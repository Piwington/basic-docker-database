from flask import Flask
import json
import psycopg2
server = Flask(__name__)


def postgres_connection():
    connection = psycopg2.connect(
        database="postgres",
        user="user",
        password="password",
        host="host.docker.internal"
    )
    return connection


def crud_sorter(crud, row):
    if "user_id" in row.keys():
        user_id = row["user_id"]
        if crud == "u":
            row.pop("user_id")

    connection = None
    cursor = None
    message = "Operation Successful: "
    try:
        connection = postgres_connection()
        cursor = connection.cursor()
        if crud == "c":
            values = (row["forename"], row["surname"], row["email"], row["phone_number"])
            cursor.execute(
                "INSERT INTO system_users (forename, surname, email, phone_number) VALUES (%s, %s, %s, %s)", values
            )
            message += "Created User With. Forename - %s, Surname - %s, Email - %s, Phone Number - %s" % values
        elif crud == "r":
            select = "SELECT * FROM system_users WHERE"
            values = ()
            first = True
            for column in row.keys():
                if column in ['user_id', 'forename', 'surname', 'email', 'phone_number']:
                    if first:
                        first = False
                    else:
                        select += " AND"
                    select += " " + column + " = %s"
                    new_pair = tuple(row[column])
                    values = values + new_pair

            cursor.execute(select, values)
            database_rows = cursor.fetchall()
            outputs = "Selected Users. "
            for row in database_rows:
                outputs += "ID - %s, Forename - %s, Surname - %s, Email - %s, Phone Number - %s" %\
                           (row[0], row[1], row[2], row[3], row[4])
        elif crud == "u":
            for column in row.keys():
                if column in ['forename', 'surname', 'email', 'phone_number']:
                    update = "UPDATE system_users SET " + column + " = %s WHERE user_id = %s"
                    cursor.execute(update, (row[column], user_id))
            message += "Updated User With ID - %s" % user_id
        elif crud == "d":
            cursor.execute("DELETE FROM system_users WHERE user_id = %s", user_id)
            message += "Deleted User With ID - %s" % user_id
        else:
            return "Unknown Operation"

        connection.commit()
        return message
    except Exception as e:
        return e
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


@server.route("/<crud>/<row>")
def hello(crud, row):
    prepped = json.loads(row)
    outcome = crud_sorter(crud, prepped)
    return "Hello Hell! %s + %s = %s" % (crud, row, outcome)


if __name__ == "__main__":
    server.run(host='0.0.0.0')
# crud_sorter("c", {"user_id": "2", "forename": "D", "surname": "C", "email": "@", "phone_number": "065"})
