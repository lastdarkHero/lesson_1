import sqlite3
from dataclasses import dataclass

# Легкий вариант

@dataclass
class User:
    name: str
    age: int
    gender: str

# Сложный вариант

# class User:
#     def __init__(self, name: str, age: int, gender: str):
#         self.name = name
#         self.age = age
#         self.gender = gender
        

# CЛОЖНЫЙ ВАРИАНТ

# try:
#     connection = sqlite3.connect("sqlite.db")
# except sqlite3.DatabaseError:
#     print("Произошла ошибка при под ключении")
# finally: #ВСЕГДА
#     connection.close()

def create_user_table(cur: sqlite3.Cursor):
    command = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT) 
    """
    cur.execute(command)


def add_user(cur: sqlite3.Cursor, user: User):
    command = """
    INSERT INTO users(name, age, gender) VALUES (?, ?, ?)
    """
    cur.execute(command, (user.name, user.age, user.gender))

def get_all_user(cur: sqlite3.Cursor):
    command = """
    SELECT * FROM users
    """
    result = cur.execute(command)
    return result.fetchall()

def updet_user_name(cur: sqlite3.Cursor, user_id: int, name: str):
    command = """
    UPDATE users Set name = ? WHERE id = ?
    """
    cur.execute(command, (name, user_id))

def get_users_by_id(cur: sqlite3.Cursor, user_id: int):
    command = """
    SELECT * FROM users WHERE id = ?
    """
    result = cur.execute(command, (user_id,))
    return result.fetchone()

def delete_all_users(cur: sqlite3.Cursor):
    command = """
    DELETE FROM users
    """
    cur.execute(command)


if __name__ == "__main__":
# ЛЕГКИЙ ВАРИАНТ

    with sqlite3.connect("sqlite.db") as connection:
        cursor = connection.cursor()
        create_user_table(cursor)
        delete_all_users(cursor)
        sergey = User(name="Сережа", age=16, gender="М")
        ira = User(name="Ира", age=17, gender="Ж")
        add_user(cursor, sergey)
        add_user(cursor, ira)
        users = get_all_user(cursor)
        print(users)
        updet_user_name(cursor, 1, "Никита")
        users = get_all_user(cursor)
        print(users)
        users = get_users_by_id(cursor, 2)
        print(users)
