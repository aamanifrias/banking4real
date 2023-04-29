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
    print(f'Welcome to Bank4Real, the realest bank of them all!')
    print("How may we assist you today? Choose an option Below.")
    client = input("(Deposit, Withdraw, Balance, Create Account, Close Account, Modify):")
    if client.lower() == "deposit":
        database_functions.deposit()
    elif client.lower() == "withdraw":
        database_functions.withdraw()
    elif client.lower() == "balance":
        database_functions.balance()
    elif client.lower() == "create account":
        database_functions.createAcc()
        
        while True:
            client2 = input("Is that all we can do for you today?")
            if client2 == "yes":
                print(f'Have a good day!')
                break
            elif client2 == "no":
                print(f'How else may we assist you?')
                break
            else: print("Try again in a moment")
