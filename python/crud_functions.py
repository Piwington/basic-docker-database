import psycopg2


def postgres_connection():
    connection = psycopg2.connect(
        database="postgres",
        user="user",
        password="password"
    )
    return connection


def crud_sorter(crud, row):
    if "user_id" in row.keys():
        user_id = row["user_id"]
        if crud == "u":
            row.pop("user_id")

    connection = None
    cursor = None

    try:
        connection = postgres_connection()
        cursor = connection.cursor()
        if crud == "c":
            cursor.execute(
                "INSERT INTO system_users (forename, surname, email, phone_number) VALUES (%s, %s, %s, %s)",
                (row["forename"], row["surname"], row["email"], row["phone_number"])
            )
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
            for row in database_rows:
                print("Id = ", row[0])
                print("Forname = ", row[1])
                print("Surname  = ", row[2])
                print("Email  = ", row[3])
                print("Phone  = ", row[4])
        elif crud == "u":
            for column in row.keys():
                if column in ['forename', 'surname', 'email', 'phone_number']:
                    update = "UPDATE system_users SET " + column + " = %s WHERE user_id = %s"
                    cursor.execute(update, (row[column], user_id))
        elif crud == "d":
            cursor.execute("DELETE FROM system_users WHERE user_id = %s", user_id)
        else:
            raise Exception

        connection.commit()
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


crud_sorter("u", {"user_id": "2", "forename": "D", "surname": "C", "email": "@"})
