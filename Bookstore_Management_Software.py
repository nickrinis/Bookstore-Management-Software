"""MAIN PROGRAM - Bookstore Management Software"""
from csv_generator import create_CSV
from login_system import login
from admin_menu import adminMenu
from user_menu import userMenu
from csv_export import export_CSV, read_UserCSV, read_AdminCSV, read_BooksCSV

#creating the csv files if they don't exist
create_CSV()

#Creating the 3 DataFrames from the .csv files
user_df = read_UserCSV()
admin_df = read_AdminCSV()
books_df = read_BooksCSV()

#Logging in/Registering the user
logged_in = 0
user_df, logged_in = login(user_df, admin_df)

#Admin Options
if logged_in in range(50, 60):
    user_df, books_df = adminMenu(user_df, admin_df, books_df, logged_in)

#User Options
elif logged_in in range(10, 50):
    user_df, books_df = userMenu(user_df, books_df, logged_in)
    
#Exporting the files
export_CSV(user_df, admin_df, books_df)