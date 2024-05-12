"""ADMIN MENU"""
import pandas as pd
from admin_use_cases import singleEntry, csvEntry, dataEdit, deleteEntry, exportToCSV, checkAvailability, checkAvailabilityPerBookstore, bookCost, totalCost, generateGraph, deleteUser, deleteComment

def adminMenu(user_df, admin_df, books_df, logged_in):
    menu = 1
    
    while not menu == 0:
        print("\nADMIN MENU:\n")
        print("1. Load a new csv file for certain books.")
        print("2. Add a book to the book dataFrame.")
        print("3. Edit an entry in the dataFrame.")
        print("4. Delete an entry from the dataFrame.")
        print("5. Get the updated book dataFrame in the form of a .csv file.")
        print("6. Check the availability of a book based on the title.")
        print("7. Check the availability of a book based on the title in certain bookstores.")
        print("8. Calculate the cost of a book.")
        print("9. Calculate the cost of all available books.")
        print("10. Generate a graph.")
        print("11. Delete a user.")
        print("12. Delete a comment")
        print("0. To exit.")
        
        menu = int(input("-> "))
        
        if menu == 1:
            csvEntry(books_df)
            #reading the reloaded csv file
            books_df = pd.read_csv("books.csv")
            print("****************************************************************************")
        
        elif menu == 2:
            books_df = singleEntry(books_df)
            print("****************************************************************************") 
            
        elif menu == 3:
            books_df = dataEdit(books_df, admin_df, logged_in)
            print("****************************************************************************")
            
        elif menu == 4:
            books_df = deleteEntry(books_df, admin_df, logged_in)
            print("****************************************************************************")
            
        elif menu == 5:
            exportToCSV(books_df)
            print("****************************************************************************")
            
        elif menu == 6:
            checkAvailability(books_df)
            print("****************************************************************************")
            
        elif menu == 7:
            checkAvailabilityPerBookstore(books_df)
            print("****************************************************************************")
        
        elif menu == 8:
            bookCost(books_df)
            print("****************************************************************************")
            
        elif menu == 9:
            totalCost(books_df)
            print("****************************************************************************")
            
        elif menu == 10:
            generateGraph(user_df, books_df)
            print("****************************************************************************")
            
        elif menu == 11:
            user_df = deleteUser(user_df)
            print("****************************************************************************")
        
        elif menu == 12:
            books_df = deleteComment(books_df)
            print("****************************************************************************")
        
        elif menu == 0:
            break
        
        else:
            print("Incorrect input...")
            print("***************************************************************")
        
    return user_df, books_df