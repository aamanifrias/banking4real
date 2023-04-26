import mysql.connector
import random

connection = mysql.connector.connect(
    user ='root',
    database = 'banking',
    password = 'amoneyHHS33!'
)
cursor = connection.cursor()

def balance():
    bankid = int(input("Enter your Bank ID: "))
    bankpin = int(input("Enter your Bank Pin: "))
    cursor.execute(f'SELECT balance FROM bankinfo WHERE bankid = {bankid} AND bankpin ={bankpin}')
    for item in cursor:
        print(f'Current Balance: ${item[0]}')
    print()

def deposit():
    bankid = int(input("Enter your Bank ID: "))
    bankpin = int(input("Enter your Bank Pin: "))
    while True:
        amtdep = int(input("Enter the amount you would like to Deposit: "))
        if amtdep < 0:
            print("Please Enter an amount greater than 0")
        else:
            break
    cursor.execute(f'UPDATE bankinfo SET balance = balance + {amtdep} WHERE bankid = {bankid} AND bankpin = {bankpin}')
    cursor.execute(f'SELECT balance FROM bankinfo WHERE bankid = {bankid} AND bankpin = {bankpin}')
    for item in cursor:
        print(f'${amtdep} was sucessfully deposited')
        print(f'Current Balance: ${item[0]}')
    print()
    connection.commit()
