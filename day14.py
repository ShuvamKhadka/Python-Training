# """
# ACID properties:
# Atomicity, Consistency, Isolation, Durability
# """

# """

# try:
#     balance add
#     balance ded.
#     commit
# except Exception:
#     rollback()
# """

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

class Database:
    def insert_info(self, con):
        try:
            query = "insert into acid1(name, balance) values (%s, %s)"
            name = input("Enter your name:")
            balance = input("Enter the balance:")
            params = [name, balance]
            con.cursor.execute(query, params)
            con.conn.commit()

        except Exception as exe:
            print(exe)

class Deposit(Connection):
    def deposit(self):
        try:
            query = "update acid1 set balance = balance + %s where id = %s"
            id = int(input("input Customer id: "))
            add_balance = float(input("Add balance: "))
            params = [add_balance, id]
            self.cursor.execute(query, params)
            self.conn.commit()
        except Exception as exe:
            print("failed query", exe)

class Withdraw(Connection):
    def withdraw(self):
        try:
            id = int(input("enter customer id: "))
            sub_balance = float(input("Withdraw balance: "))
            query = "update acid1 set balance = balance - %s where id = %s"
            params = [sub_balance, id]
            self.cursor.execute(query, params)
            self.conn.commit()
        except Exception as exe:
            print("Failed Query", exe)

class Transaction(Connection):
    def transact(self):
        try:
            sender = int(input("Enter sender id: "))
            receiver = int(input("Enter receiver id: "))
            transfer_amount = float(input("Enter the transfer amount: "))
            query1 = "update acid1 set balance = balance + %s where id = %s"
            params1 = [transfer_amount, receiver]
            query2 = "update acid1 set balance = balance - %s where id =%s"
            params2 = [transfer_amount, sender]
            self.cursor.execute(query1, params1)
            self.cursor.execute(query2, params2)
            self.conn.commit()
        except Exception as exe:
            self.conn.rollback()
            print("Failed Query", exe)

class GetInfo(Connection):
    def get_info(self):
        try:
            query = "select * from acid1"
            params = []
            self.cursor.execute(query, params)
            row = self.cursor.fetchone()
            print(row)
            self.conn.commit()

        except Exception as exe:
            print(exe)  



# con = Connection()
# db = Database()
# db.insert_info(con)

g1 = GetInfo()
g1.get_info()

t1 = Transaction()
t1.transact()            

