import psycopg2

class Connection:
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

class Student:
    def __init__(self, email):
        try:
            self.email = email
        except Exception as exe:
            print(exe)
    def insert_student(self, con):
        try:
            query = "insert into std(name, address, mobile_number, email) VALUES(%s, %s, %s, %s)"
            name = input("enter the name:")
            address = input("enter the address:")
            mobile_number = input("enter the mobile_number:")
            email = input("enter the email:")
            params = [name, address, mobile_number, email]
            con.cursor.execute(query, params)
            con.conn.commit()
        except Exception as exe:
            print(exe)

    def select_student(self, con):
        try:
            query = "Select * from std"
        except Exception as exe:
            print(exe)
    
    def validate(self):
        try:
            if "@" in self.email and self.email.islower():
                print("valid email")
            else:
                print("Invalid email")
        except Exception as exe:
            print(exe)


con = Connection()
db = Student("email")
db.insert_student(con)
db.validate()