import mysql.connector


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
        print(f'New Balance: ${item[0]}')
    print()

def createAcc():
    newID = int(input(f'Enter a unique Bank ID:  '))
    newPin = int(input(f'Enter a unique Bank Pin:  '))
    namie = input(f'Enter a Name: ')
    bal = int(input(f'Enter an intial Balance: '))
    youngness = int(input(f'Enter a age: '))
    if youngness < 18:
        print(f'Too young to create an account.')
    cursor.execute(f'UPDATE bankinfo SET bankid = newID, bankpin = newPin, name = namie, balance = bal, age = youngness WHERE  ')

def withdraw():
    bankid = int(input("Enter your Bank ID: "))
    bankpin = int(input("Enter your Bank Pin: "))
    while True:
        cursor.reset()
        amtwithdraw = int(input("How much would you like to withdraw from your account? "))
        cursor.execute(f'SELECT balance FROM bankinfo WHERE bankid = {bankid} AND bankpin = {bankpin}')
        intial = 20
        for item in cursor:
            for thing in cursor:
                intial = thing
        if amtwithdraw < intial and amtwithdraw > 0:
            cursor.execute(f'UPDATE bankinfo SET balance = balance - {amtwithdraw} WHERE bankid = {bankid} AND bankpin = {bankpin}')
            cursor.execute(f'SELECT balance FROM bankinfo WHERE bankid = {bankid} AND bankpin = {bankpin}')
            for item in cursor:
                print(f'Successfully widthdrew ${amtwithdraw} The new balance for bank number {bankid} is {item[0]}.')
            connection.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!
            break
        else:
            print("The amount of money you're trying to withdraw is larger than your balance, please try again.")


    connection.commit()
