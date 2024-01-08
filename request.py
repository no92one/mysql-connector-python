import mysql.connector

database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="linus123",
    database="Python_test_data"
)
cursor = database.cursor(dictionary=True)


def get_all_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


def add_user(username, password):
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    database.commit()


def remove_user_by_id(user_id):
    cursor.execute(f"DELETE FROM users WHERE id={user_id}")
    database.commit()
