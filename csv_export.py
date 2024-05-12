import pandas as pd


def export_CSV(user_df, admin_df, books_df):
    # exporting as csv
    with open("user.csv", 'w', newline=""):
        user_df.to_csv("user.csv", index=False)
        
    with open("admin.csv", 'w', newline=""):
        admin_df.to_csv("admin.csv", index=False)
        
    with open("books.csv", 'w', newline=""):
        books_df.to_csv("books.csv", index=False)
    
    # exporting as json
    user_df.to_json('./user.json', orient='index')
    
    admin_df.to_json('./admin.json', orient='index')
    
    books_df.to_json('./books.json', orient='index')


# reading the user csv file
def read_UserCSV():
    user_df = pd.read_csv("user.csv")
    return user_df


# reading the admin csv file
def read_AdminCSV():
    admin_df = pd.read_csv("admin.csv")
    return admin_df


# reading the books csv file
def read_BooksCSV():
    books_df = pd.read_csv("books.csv")
    return books_df
