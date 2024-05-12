"""LOGIN SYSTEM"""
# Logs in the user as admin/user or signs them up as user
import pandas as pd
import sys


def login(user_df, admin_df):
    
    logged_in = 0
    new_id = 0
    specialCharacters = "!@#$%^&*()-+?_=,<>/"
    check = 0
    
    # Menu
    while check == 0:
        menu = int(input("Please enter: \n1. If you wish to login as an administrator.\n2. If you wish to login as a user.\n3. If you wish to create an account.\n...\n"))
        if 1 <= menu <= 3:
            check = 1
        else:
            print("Input must be 1, 2 or 3...")
       
    # Admin login
    if menu == 1:
        # flags
        correct_username = 0
        correct_password = 0
        pw_check = 0
        error = 0
        
        # columns with the data we need
        udata = admin_df.loc[:, ["id", "username", "password"]]
        
        while correct_username == 0:
            username = (input("Please enter your username: "))
            
            for ID, name, pword in udata.itertuples(index=False):
                # If password and username are correct change flags and save ID
                if username == name:
                    correct_username = 1
                    while pw_check == 0:
                        password = (input("Please enter your password: "))
                        if password == pword:
                            correct_password = 1
                            pw_check = 1
                        else:
                            print("Incorrect password!")
                            error += 1
                            if error == 3:
                                print("You've reached the maximum login attempts, exiting...")
                                sys.exit()
                        
                if correct_username and correct_password == 1:
                    logged_in = ID
                correct_password = 0
            
            if correct_username == 0:
                print("Incorrect username...")
        
        if not logged_in == 0:
            print("Welcome, "+username+"!")   
        return user_df, logged_in
        
    # User login
    elif menu == 2:
        # flags
        correct_username = 0
        correct_password = 0
        pw_check = 0
        error = 0
        
        # columns with the data we need
        udata = user_df.loc[:, ["id", "username", "password"]]
        
        while correct_username == 0:
            username = (input("Please enter your username: "))
            
            for ID, name, pword in udata.itertuples(index=False):
                # If password and username are correct change flags and save ID
                if username == name:
                    correct_username = 1
                    while pw_check == 0:
                        password = (input("Please enter your password: "))
                        if password == pword:
                            correct_password = 1
                            pw_check = 1
                        else:
                            print("Incorrect password!")
                            error += 1
                            if error == 3:
                                print("You've reached the maximum login attempts, exiting...")
                                sys.exit()
                        
                if correct_username and correct_password == 1:
                    logged_in = ID
                correct_password = 0
            
            if correct_username == 0:
                print("Incorrect username...")
            
        if not logged_in == 0:
            print("Welcome, "+username+"!")   
        return user_df, logged_in

    # User registration
    else:
        correct_username = 0
        correct_password = 0
        containsSpecialCharacter = 0
        passwordLength = 0
        udata = user_df.loc[:, ["id", "username", "password"]]
        
        while correct_username == 0:
            unique = 1
            username = (input("Please enter your username: "))
            for ID, name, pword in udata.itertuples(index=False):
                if username == name:
                    unique = 0
            if not unique == 0:
                correct_username = 1
            else:
                print("Username is taken, please choose another.")
                    
        while correct_password == 0:
            unique = 1
            password = (input("Please enter your password: "))
            if any(character in specialCharacters for character in password):
                containsSpecialCharacter = 1
            if len(password) >= 8:
                passwordLength = 1
            
            for ID, name, pword in udata.itertuples(index=False):
                if password == pword:
                    unique = 0
            if unique == 1 and containsSpecialCharacter == 1 and passwordLength == 1:
                correct_password = 1
            else:
                print("Password must be unique, have at least 8 characters and 1 special character, please enter a new password.")
                
        password_ver = (input("Please enter your password again: "))
        
        if not password == password_ver:
            print("Passwords must much! exiting...")
            sys.exit()
        else:
            for ID, name, pword in udata.itertuples(index=False):
                new_id = ID+1
            logged_in = new_id
            
            registered = 0
            
            while registered == 0:
                data = input("Would you like to enter additional data (address, city, orders, favorites, balance)? \n[y/n]\n")
                
                if data == "y":
                    address = input("Please enter your address: ")
                    city = input("Please enter your city: ")
                 
                    orders = []
                    order_number = int(input("Please enter how many orders you would like to make:"))
                    for number in range(order_number):
                        orders.append(int(input("Please enter the book you liked [101-]: ")))

                    favorites = []
                    favorites_number = int(input("Please enter how many favorite books you have:"))
                    for number in range(favorites_number):
                        favorites.append(int(input("Please enter the book you liked [101-]: ")))
                    
                    balance = float(input("Please enter your balance:"))
                    
                    register_header = ['id', 'username', 'password', 'address', 'city', 'orders', 'favorites', 'balance']
                    register_data = [[logged_in, username, password, address, city, orders, favorites, balance]]
                    register_df = pd.DataFrame(register_data, columns=register_header)
                    
                    registered = 1
                    
                elif data == "n":
                    register_header = ['id', 'username', 'password', 'address', 'city', 'orders', 'favorites', 'balance']
                    register_data = [[logged_in, username, password, "Default 3", "Lamia", [102], [101], 100.0]]
                    register_df = pd.DataFrame(register_data, columns=register_header)
                    
                    registered = 1
            
            return_df = user_df.append(register_df, ignore_index=True)
            
            print("Registered Successfully!")
            return return_df, logged_in
