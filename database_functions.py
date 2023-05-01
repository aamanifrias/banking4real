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
    nombre = str(input("Enter the name of the Account Holder: "))
    cursor.execute(f'SELECT balance FROM bankinfo WHERE bankid = {bankid} AND bankpin ={bankpin} AND name = \"{nombre}\"')
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
    cursor.reset()
    newID = int(input(f'Enter a unique Bank ID:  '))
    newPin = input(f'Enter a unique Bank Pin:  ')
    namie = input(f'Enter a Name: ')
    bal = int(input(f'Enter an intial Balance: '))
    youngness = int(input(f'Enter a age: '))
    cursor.execute(f'INSERT INTO bankinfo (bankid, name, balance, age, bankpin) VALUES ({newID}, \"{namie}\", {bal}, {youngness}, \"{newPin}\")')
    
    connection.commit()

def deleteAcc():
    cursor.reset()
    bankid = int(input("Please enter your Bank Account ID: "))
    bankpin = int(input("Please enter the Account's PIN: "))
    while True:
        validSeq = str(input(f'Are you sure you want to Delete this Account?'))
        if validSeq == "yes":
            cursor.execute(f'DELETE FROM banking.bankinfo WHERE bankid = {bankid} AND bankpin = {bankpin}')
            print("\nUser account successfully deleted.")
            break
    connection.commit()

def modify():
    #cursor.reset()
    bankid = int(input("Please enter your Bank Accoun ID: "))
    bankpin = int(input("Please enter the Account's PIN: "))
    bankname = str(input("Please enter the name of the Account Holder: "))
    while True:
        newClient = str(input("Enter the new name of the account: "))
        if len(newClient) > 0:
            break
        else:
            print("Please enter a name.")
    cursor.execute(f'UPDATE banking.bankinfo SET name = \"{newClient}\" WHERE bankid = {bankid} AND bankpin = {bankpin}')
    print(f"\nSuccessfully changed the name of user account from {bankname} to {newClient}")
    connection.commit()
    



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
            connection.commit()
            break
        else:
            print("The amount of money you're trying to withdraw is larger than your balance, please try again.")


    connection.commit()
