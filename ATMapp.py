import random

database = {
    9802758755: ['Daniel', 'Ukene', 'evanaukene@gmail.com', 'Password', 0]
}


def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have an account with us: 1(yes) 2 (no) \n"))

    if have_account == 1:
        login()
    elif have_account == 2:
        print(register())
    else:
        print("You have selected an invalid option!")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("what is your account number? \n")

    is_valid_account_number = account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = input("What is your password \n")

        for account_number, userDetails in database.items():
            if account_number == int(account_number_from_user):
                if userDetails[3] == password:
                    bank_operation(userDetails)
                else:
                    print('Invalid account or password')
                    login()
    else:
        init()


def account_number_validation(account_number):
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid Account number, account number should be integer")
                return False

        else:
            print("Account Number cannot be less or more than 10 digits")
            return False
    else:
        print("Account Number is a required field")
        return False


def register():
    print("****** Register ******")
    email = input("What is your email address?\n")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    password = input("Create a password for yourself? \n")

    account_number = generate_account_number()

    database[account_number] = [first_name, last_name, email, password]

    print("Your account has been created")
    print("================================")
    print(f"Your account number is {account_number}")
    print("Make sure you keep it safe")
    print("==================================")
    login()


def bank_operation(user):
    print(f"Welcome {user[0]} {user[1]}")

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) exit\n"))

    if selected_option == 1:
        deposit_operation()
    elif selected_option == 2:
        withdrawal_operation()
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        exit()
    else:
        print("Invalid option selection")
        bank_operation(user)


def deposit_operation():
    amount_to_deposit = int(input("How much do you want to deposit: "))
    for account_number, userDetails in database.items():
        userDetails[4] += amount_to_deposit
        print(f"Your available balance is now {userDetails[4]}")
    withdraw_after_deposit()


def withdrawal_operation():
    amount_to_withdraw = int(input("How much do you want to withdraw: "))

    for account_number, userDetails in database.items():
        if userDetails[4] >= amount_to_withdraw:
            userDetails[4] -= amount_to_withdraw
            print(f"Your balance is now {userDetails[4]}")
        else:
            print("Insufficient Funds")
            withdrawal_operation()


def withdraw_after_deposit():  # this function provides the user an option to withdraw after depositing some money
    next_step = int(input("What would you like to do now? \n(1) Withdraw \n(2) Exit \n"))
    if next_step == 1:
        withdrawal_operation()
    elif next_step == 2:
        exit()
    else:
        print("Invalid option selection")
        withdraw_after_deposit()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def logout():
    login()


init()
