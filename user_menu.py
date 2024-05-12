"""USER MENU"""
import pandas as pd
from user_use_cases import csvEntry, singleEntry, editData, emptyFavorites, checkBalance, checkBookAvail, checkOrders, editOrders, checkCopies, getSuggestions, makeComment

def userMenu(user_df, books_df, logged_in):
    menu = 1
    
    while not menu == 0:
        print("\nUSER MENU:\n")
        print("1. Load a new csv file for books you would like.")
        print("2. Add book you would like.")
        print("3. Edit your personal data.")
        print("4. Empty your favorites list.")
        print("5. Check your balance.")
        print("6. Check the availability and price of books in your favorites.")
        print("7. See all your orders.")
        print("8. Manage your orders.")
        print("9. Check the total amount of copies of a book that you can purchase.")
        print("10. Get suggestions.")
        print("11. Make a comment.")
        print("0. To exit.")
        
        menu = int(input("-> "))
        
        if menu == 1:
            csvEntry(user_df, books_df, logged_in)
            #reading the reloaded csv file
            user_df = pd.read_csv("user.csv")
            print("***************************************************************")
        
        elif menu == 2:
            user_df = singleEntry(user_df, books_df, logged_in)
            print("***************************************************************")
            
        elif menu == 3:
            user_df = editData(user_df, logged_in)
            print("***************************************************************")
            
        elif menu == 4:
            user_df = emptyFavorites(user_df, logged_in)
            print("***************************************************************")
            
        elif menu == 5:
            checkBalance(user_df, logged_in)
            print("***************************************************************")
            
        elif menu == 6:
            checkBookAvail(user_df, books_df, logged_in)
            print("***************************************************************")
            
        elif menu == 7:
            checkOrders(user_df, books_df, logged_in)
            print("***************************************************************")
        
        elif menu == 8:
            user_df, books_df = editOrders(user_df, books_df, logged_in)
            print("***************************************************************")
            
        elif menu == 9:
            checkCopies(user_df, books_df, logged_in)
            print("***************************************************************")
            
        elif menu == 10:
            getSuggestions(user_df, books_df, logged_in)
            print("***************************************************************")
            
        elif menu == 11:
            books_df = makeComment(user_df, books_df, logged_in)
            print("***************************************************************")

        elif menu == 0:
            break
        
        else:
            print("Incorrect input...")
            print("***************************************************************")
        
    return user_df, books_df