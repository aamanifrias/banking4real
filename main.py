import mysql.connector
import database_functions
import os

os.system('cls')
connection = mysql.connector.connect(
    user ='root',
    database = 'banking',
    password = 'amoneyHHS33!'
)

cursor = connection.cursor()
print("-~-~-~-~-BANK4REAL-~-~-~-~-")

while True:
    client = input("Choose an option(Deposit, Withdraw, Balance, Create Account, Close Account, Modify): )")
    if client.lower() == "deposit":
        database_functions.deposit()
        while True:
            client2 = input("Is that all we can do for you today?")
            if client2 == "yes":
                break
            elif client2 == "no":
                break
            else: print("Try again in a moment")