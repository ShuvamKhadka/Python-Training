import psycopg2

class Student:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host = "localhost",
                database = "test",
                user = "postgres",
                password = "1910",
                port = "5432"
            )
            self.cursor = self.conn.cursor()
            print("Connection success.")
        except Exception as exe:
            print("Connection fail", exe)
    def insert_student(self):
        try:
            query = "insert into std(name, address, mobile_number, email) VALUES(%s, %s, %s, %s)"
            name = input("enter the name:")
            address = input("enter the address:")
            mobile_number = input("enter the mobile_number:")
            email = input("enter the email:")
            params = [name, address, mobile_number, email]
            self.cursor.execute(query, params)
            self.conn.commit()
        except Exception as exe:
            print(exe)

db = Student()
db.insert_student()