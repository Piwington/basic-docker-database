import psycopg2


def postgres_connection():
    connection = psycopg2.connect(
        database="postgres",
        user="user",
        password="password"
    )
    return connection


def postgres_insert(row):
    connection = None
    cursor = None
    try:
        connection = postgres_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO system_users (forename, surname, email, phone_number) VALUES (%s, %s, %s, %s)",
            (row["forename"], row["surname"], row["email"], row["phone_number"])
        )
        connection.commit()
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


postgres_insert({"forename": "A", "surname": "B", "email": "@", "phone_number": "099"})
