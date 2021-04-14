#Auth Part
import random
from datetime import datetime


database = {}
account_numbers = set()


def check_balance(user):
    print(f'Your account balance is: {user["balance"]}')
    return bank_operations(user)

def withdraw(user):
    cash = int(input('How much would you like to withdraw? \n'))
    try:
        if user['balance'] - abs(cash) < 0:
            print(f'Your account balance is: {user["balance"]}')
            print('You do not have enough money for this withdrawal. Please try again.')
            return withdraw(user)
        else:
            user['balance'] -= cash
            print(f'Please, take your cash')
            return bank_operations(user)
    except:
        print('You have selected an invalid amount, please try again')
        return withdraw(user)

def deposit(user):
    amount = input(f'How much would you like to deposit? \n')
    try:
        user['balance'] += int(amount)
        print(f'Your balance is now: {userBalance[user]}')
        return bank_operations(user)
    except:
        print('You have inputed an invalid amount')
        return deposit(user)
        
def complaint(user):
    issue = input(f'What issue would you like to report? \n')
    if isinstance(issue, str):
        user['complaints'].append(issue)
        print('Thank you for contacting us')
        return bank_operations(user)
    else:
        return f'Please make a valid complaint'
        complaint(user)


def account_number_generator(email: str, account_numbers):
    #generates a 10 digit unique account number for each user using his/her email
    random.seed(email)
    number = random.randint(1000000000,9999999999)
    
    check = len(account_numbers)
    account_numbers.add(number)

    #make sure generated account number is unique
    if len(account_numbers) > check:
        return number
    else:
        number += 1
        return number

#Register user in bank app
def register(database):
    first_name  = input('Please type in your first name below: \n')
    last_name   = input('Please type in your last name below: \n')
    email       = input('Please type in your email below: \n')
    password    = input('Please type in your password below: \n')

    account_number = account_number_generator(email, account_numbers)
    
    database[account_number] = {'first_name': first_name,
                                'last_name': last_name, 
                                'email': email, 
                                'password': password, 
                                'balance': 0, 
                                'complaints': []}
    print()
    print(f'Welcome to bankPHP {first_name + " " + last_name}, your account number is: {account_number}')
    print('Please store your account number in a safe place')
    print("================================================\n")

    log_in = int(input('Do you wish to login to your account? 1 - Yes, 2 - No \n'))

    if log_in == 1:
        login(database)
    elif log_in ==2:
        print('Thank you for banking with us.')
    else:
        print('Invalid option selected.')
        initialize(database)
        

#Login to bank app
def login(database):
    print('Login to your account \n')
    user = int()
    user_account_number = int(input('What is your account number? \n')) 

    if database[user_account_number]:
        user = database[user_account_number]
    else:
        print('This account number does not exist, please try again.')
        login(database)

    def password_check(user):
        user_account_password = str(input('Please type in you password. \n'))

        if user_account_password == user['password']:     
            print()
            print(f'Welcome {user["first_name"]}, you have successfully logged in.')
            bank_operations(user)
        else:
            print('You have entered an incorrect password, please try again.')
            print("================================================\n")
            password_check(user)
        
    password_check(user)


#Perform banking operations
def bank_operations(user):
    print('======================================')
    print(f'Today is: {datetime.now().strftime("%Y-%m-%d : %H:%M:%S")}')
    print(f'\nThese are the available options:')
    print(f'1.    Withdrawal')
    print(f'2.    Cash Deposit')
    print(f'3.    Check Balance')
    print(f'4.    Complaint')
    print(f'5.    Logout')
    print()
    selectedOption = int(input('Please select an option: \n'))

    if selectedOption == 1:      
        x = withdraw(user)
        print(f'\n {x}')

    elif selectedOption == 2:       
        x = deposit(user)
        print(f'\n{x}')

    elif selectedOption == 3:        
        x = check_balance(user)
        print(f'\n{x}')

    elif selectedOption == 4:       
        x = complaint(user)
        print(f'\n{x}')

    elif selectedOption == 5:
        print('Thank you for banking with us.')
        initialize(database)
    else:
        print(f'\nInvalid option selected, please try again.')
        bank_operations(user)


#Initializing the bank app
def initialize(database):
    print('Welcome to bankPHP')
    option_validator = False

    while option_validator == False:
        account_check = int(input('Do you have and account with us?: 1 - Yes, 2 -No \n'))

        if account_check == 1:
            option_validator = True
            login(database)

        elif account_check == 2:
            option_validator = True
            register(database)

        else:
            print('You have selected an invalid option, please try again \n')



### RUN THE BANK APP ###

initialize(database)