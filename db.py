import sqlite3

# see local-storage on notion coding-challenges


class DataBase:
    def __init__(self, ID=1):
        self.ID = ID

    # Q2
    def insert_users(self, name, email, age):
        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()

        # presence check (email is unique field in db)
        cursor.execute("SELECT 1 FROM Users WHERE Email = ?", (email,))
        if cursor.fetchone():
            print(f"User with email {email} already exists.")

        query = "INSERT INTO Users (Name, Email, Age) VALUES (?,?,?)"
        cursor.execute(
            query,
            (name, email, age),
        )

        conn.commit()
        conn.close()

    def select(self, table, field="*", clause="ID = ?", var=1):
        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()

        if (table == "Users" and field == "*") or clause == "-":
            query = f"SELECT {field} FROM {table}"
            cursor.execute(query)
        else:
            # TODO: make dynamic not fixed to ID
            query = f"SELECT {field} FROM {table} WHERE {clause}"
            cursor.execute(query, (var,))

        result = cursor.fetchall()

        conn.close()

        return result

    def update(self, table, field, value, value2=""):
        if field.lower() == "id":
            return

        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()
        query = f"UPDATE {table} SET {field} = ? WHERE ID = ?"

        v2 = self.ID if value2 == "" else value2

        cursor.execute(query, (value, v2))
        conn.commit()

        conn.close()

    def delete(self, table, field="*", value=""):
        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()

        if field == "*" and value == "":
            query = f"DELETE FROM {table}"
            cursor.execute(query)
        else:
            query = f"DELETE FROM {table} WHERE {field} = ?"
            cursor.execute(query, (value,))

        conn.commit()
        conn.close()
