"""ADMIN USE CASES"""
import pandas as pd
import numpy as np
import ast
from matplotlib import pyplot as plt

"""CASE 2"""
def singleEntry(books_df):
    bdata = books_df.loc[:,["id", "title"]]
    correct_name = 0
    book_id = 0
    #Check for title, id
    while correct_name == 0:
        book_title = (input("Please enter the title of the book you wish to add: "))
        name_exists = 0
        
        for ID, title in bdata.itertuples(index=False):
            new_id = ID+1
            if book_title == title:
                print("The book already exists in the data frame! ")
                name_exists = 1
        
        if name_exists == 0:
            correct_name = 1
    #Get data
    book_id = new_id
    author = (input("Please enter the name of the Author: "))
    publisher = (input("Please enter the name of the Publisher: "))
        
    categories = []
    categories_number = int(input("Enter the number of categories for the book: "))
    for number in range(categories_number):
        categories.append(input("-Enter a category for the book: "))
        
    cost = float(input("Please enter the cost of the Book: "))
    shipping_cost = float(input("Please enter the shipping cost of the book: "))
    availability_check = (input("Please enter if the book is available or not [True/False]:"))
    if availability_check == 'True':
        availability = True
    else:
        availability = False
    copies = int(input("Please enter the number of copies of the book: "))
        
    bookstores = {}
    bookstore_number = int(input("Enter the number of bookstores the book is in: [1-5]:"))
    for number in range (0, bookstore_number):
        key = int(input("-Enter the bookstore id [1-5]: "))
        value = int(input("-Enter the amount of copies in the bookstore: "))
        bookstores[key] = value
        
    rating = np.nan
    #create new df
    entry_header = ['id', 'title', 'author', 'publisher', 'categories', 'cost', 'shipping_cost', 'availability', 'copies', 'bookstores', 'rating']
    entry_data = [[book_id, book_title, author, publisher, categories, cost, shipping_cost, availability, copies, bookstores, rating]]
    entry_df = pd.DataFrame(entry_data, columns=entry_header)
    
    return_df = books_df.append(entry_df, ignore_index = True)
    print("Entry added succesfully!")
    return return_df
    
"""CASE 1"""
def csvEntry(books_df):
    #new df data
    bdata = books_df.loc[:,["id", "title"]]
    entry_header = ['id', 'title', 'author', 'publisher', 'categories', 'cost', 'shipping_cost', 'availability', 'copies', 'bookstores', 'rating']
    entry_data = []
    #number of entries
    add_num = int(input("Please enter the number of books you wish to add to the new csv file: "))
    
    for df_number in range(0, add_num):
        correct_name = 0
        book_id = 0
        #name check
        while correct_name == 0:
            book_title = (input("Please enter the title of the book you wish to add: "))
            name_exists = 0
            
            for ID, title in bdata.itertuples(index=False):
                new_id = ID+1
                if book_title == title:
                    print("The book already exists in the data frame! ")
                    name_exists = 1
            
            if name_exists == 0:
                correct_name = 1
        #get data
        book_id = new_id+df_number
        author = (input("Please enter the name of the Author: "))
        publisher = (input("Please enter the name of the Publisher: "))
            
        categories = []
        categories_number = int(input("Enter the number of categories for the book: "))
        for number in range(categories_number):
            categories.append(input("-Enter a category for the book: "))
            
        cost = float(input("Please enter the cost of the Book: "))
        shipping_cost = float(input("Please enter the shipping cost of the book: "))
        availability_check = (input("Please enter if the book is available or not [True/False]:"))
        if availability_check == 'True':
            availability = True
        else:
            availability = False
        copies = int(input("Please enter the number of copies of the book: "))
            
        bookstores = {}
        bookstore_number = int(input("Enter the number of bookstores the book is in: [1-5]:"))
        for number in range (0, bookstore_number):
            key = int(input("-Enter the bookstore id [1-5]: "))
            value = int(input("-Enter the amount of copies in the bookstore: "))
            bookstores[key] = value
            
        rating = np.nan
        #Appending the book data
        entry_data.append([book_id, book_title, author, publisher, categories, cost, shipping_cost, availability, copies, bookstores, rating])
        
    #Creating the 2 dataframes
    entry_df = pd.DataFrame(entry_data, columns=entry_header)    
    return_df = books_df.append(entry_df, ignore_index = True)
    #Reloading the csv file
    with open("books.csv", 'w', newline=""):
        return_df.to_csv("books.csv", index=False)
    
    print("CSV file loaded successfully!")

"""CASE 3"""
def dataEdit(books_df, admin_df, logged_in):
    #create dataframes
    bdata = books_df.loc[:,["id", "title", "author", "publisher", "cost", "shipping_cost", "availability", "copies", "bookstores"]]
    adata = admin_df.loc[:,["id", "bookstores"]]
    admin_bookstores = []
    book_bookstores = []
    
    #save admin bookstores
    for ID, bookstores in adata.itertuples(index = False):
        if ID == logged_in:
            admin_bookstores = bookstores
    #get last id
    for ID, title, author, publisher, cost, shipping_cost, availability, copies, bookstores in bdata.itertuples(index=False):
        maxID = str(ID)
    #get book id from admin
    edit_id = int(input("Enter the id of the book you wish to edit the data of [101-"+maxID+"]: "))
    
    for ID, title, author, publisher, cost, shipping_cost, availability, copies, bookstores in bdata.itertuples(index=False):
        if edit_id == ID:
            #making the conversions and saving bookstores that the book belongs to
            book_bookstores = str(list(ast.literal_eval(bookstores).keys()))
            #checking if they match
            if admin_bookstores == book_bookstores:
                #getting index in form of list and saving it as an integer
                i = books_df.index[books_df["id"] == edit_id].tolist()
                index = i[0]
                #Getting data
                new_title = input("Enter the new title you would like for the book: ")
                new_author = input("Enter the new author you would like for the book: ")
                new_publisher = input("Enter the new publisher you would like for the book: ")
                new_cost = float(input("Enter the new cost you would like for the book: "))
                new_shipping_cost = float(input("Enter the new shipping cost you would like for the book: "))
            
                new_availability_check = input("Enter the new availability you would like for the book [True/False]: ")
                if new_availability_check == 'True':
                    new_availability = True
                else:
                    new_availability = False
                new_copies = int(input("Enter the new amount of copies you would like for the book: "))
            
                new_bookstores = {}
                bookstore_number = int(input("Enter the new number of bookstores the book is in: [1-5]:"))
                for number in range (0, bookstore_number):
                    key = int(input("-Enter the bookstore id [1-5]: "))
                    value = int(input("-Enter the amount of copies in the bookstore: "))
                    new_bookstores[key] = value
                #Rewriting the entry with the new values
                books_df.at[index, "title"] = new_title
                books_df.at[index, "author"] = new_author
                books_df.at[index, "publisher"] = new_publisher
                books_df.at[index, "cost"] = new_cost
                books_df.at[index, "shipping_cost"] = new_shipping_cost
                books_df.at[index, "availability"] = new_availability
                books_df.at[index, "copies"] = new_copies
                books_df.at[index, "bookstores"] = new_bookstores
                
                print("Changes made successfully!")
            
            else:
                print("You do not have access to the bookstores this book is in.")
        
    return books_df

"""CASE 4"""
def deleteEntry(books_df, admin_df, logged_in):
    #create dataframes
    bdata = books_df.loc[:,["id", "bookstores"]]
    adata = admin_df.loc[:,["id", "bookstores"]]
    admin_bookstores = []
    book_bookstores = []
    
     
    #save admin bookstores
    for ID, bookstores in adata.itertuples(index = False):
        if ID == logged_in:
            admin_bookstores = bookstores
    
    #get last id
    for ID, bookstores in bdata.itertuples(index=False):
        maxID = str(ID)
    #get book id from admin
    delete_id = int(input("Enter the id of the book you wish to delete from the data frame [101-"+maxID+"]: "))
    
    for ID, bookstores in bdata.itertuples(index=False):
        if delete_id == ID:
            #making the conversions and saving bookstores that the book belongs to
            book_bookstores = str(list(ast.literal_eval(bookstores).keys()))
            #checking if they match
            if admin_bookstores == book_bookstores:
                #getting index in form of list and saving it as an integer
                i = books_df.index[books_df["id"] == delete_id].tolist()
                index = i[0]
                #droping the row at the index of the book
                books_df = books_df.drop(index)
                
                print("Book deleted successfully!")
            else:
                print("You do not have access to the bookstores this book is in.")
    
    return books_df

"""CASE 5"""
def exportToCSV(books_df):
    
    #Export the data frame as csv file
    with open("books.csv", 'w', newline=""):
        books_df.to_csv("books.csv", index=False)

    print("DataFrame exported successfully!")
    
"""CASE 6"""
def checkAvailability(books_df):
    #Create data frame
    bdata = books_df.loc[:,["title", "availability", "copies"]]
    correct_book = 0
    
    while correct_book == 0:
        hunted = (input("Please enter the title of the book you wish to check the availability of: "))
        name_exists = 0
        #Check for name and availability
        for title, availability, copies in bdata.itertuples(index=False):
            if hunted == title:
                if availability:
                    print(hunted," is available with ",copies," copies.")
                else:
                    print(hunted," is not available")
                name_exists = 1
        
        if name_exists == 1:
            correct_book = 1
        else: 
            print("The book does not exist in the data frame.")

"""CASE 7"""
def checkAvailabilityPerBookstore(books_df):
    #Create data frame
    bdata = books_df.loc[:,["title", "availability", "bookstores"]]
    correct_book = 0
    bookstore_id = []
    
    while correct_book == 0:
        hunted = (input("Please enter the title of the book you wish to check the availability of: "))
        name_exists = 0
        found = 0
        #Check for title and availability, if available get bookstore id from user
        for title, availability, bookstores in bdata.itertuples(index=False):
            if hunted == title:
                if availability:
                    bookstore_number = int(input("Please enter the amount of bookstores you wish to search for: "))
                    for number in range (0, bookstore_number):
                        bID = int(input("-Enter the bookstore id: "))
                        bookstore_id.append(bID)
                    
                    #making the conversion from json str to dict
                    converted_bookstores = ast.literal_eval(str(bookstores))
                    #cross referencing user bookstore id's with the bookstores the book is in.
                    for key,value in converted_bookstores.items():
                        for i in bookstore_id:
                            if key == i:
                                print("Bookstore id: ",key," has ",value,"copies.")
                                found = 1
                    
                    if found == 0:
                        print("The book is not in any of the bookstores you entered.")
                else:
                    print(hunted," is not available")
                name_exists = 1
        
        if name_exists == 1:
            correct_book = 1
        else: 
            print("The book does not exist in the data frame.")

"""CASE 8"""
def bookCost(books_df):
    #Create data frame
    bdata = books_df.loc[:,["title", "cost", "shipping_cost"]]
    total_book_cost = 0
    correct_book = 0
    
    while correct_book == 0:
        hunted = (input("Please enter the title of the book you wish to check the cost of: "))
        name_exists = 0
        #If the book is found calculate and show cost
        for title, cost, shipping_cost in bdata.itertuples(index=False):
            if hunted == title:
                print(hunted,"costs",cost,"€, and has a shipping cost of",shipping_cost,"€.")
                total_book_cost = cost + shipping_cost
                print("Total cost:",total_book_cost,"€")
                name_exists = 1
        
        if name_exists == 1:
            correct_book = 1
        else: 
            print("The book does not exist in the data frame.") 

"""CASE 9"""
def totalCost(books_df):
    #Create data frame
    bdata = books_df.loc[:,["author", "publisher", "cost", "shipping_cost", "availability"]]
    total_book_cost = 0
    book_cost = 0
    book_shipping = 0
    
    while True:
        #cost menu
        print("\n~COST MENU:\n")
        print("~1. Get total cost.")
        print("~2. Get total cost based on an author.")
        print("~3. Get total cost based on a publisher.")
        print("~0. To exit.")
        cost_type = int(input("-> "))
        #calculate and show total cost based on availability
        if cost_type == 1:
            for author, publisher, cost, shipping_cost, availability in bdata.itertuples(index=False):
                if availability:
                    book_cost += cost
                    book_shipping += shipping_cost
                    temp_total_cost = cost + shipping_cost
                    total_book_cost += temp_total_cost
            
            print("The cost of all available books is:",book_cost,"€, with shipping cost:",book_shipping,"€")
            print("Total cost:",total_book_cost,"€")
            #reset values
            book_shipping = 0
            book_cost = 0
            total_book_cost = 0
            
        #calculate and show total cost based on availability and author
        elif cost_type == 2: 
            author_name = input("Please enter the name of the author: ")
            
            for author, publisher, cost, shipping_cost, availability in bdata.itertuples(index=False):
                if author_name == author:
                    if availability:
                        book_cost += cost
                        book_shipping += shipping_cost
                        temp_total_cost = cost + shipping_cost
                        total_book_cost += temp_total_cost
                
            print("The cost of all available books is:",book_cost,"€, with shipping cost:",book_shipping,"€")
            print("Total cost:",total_book_cost,"€")
            #reset values
            book_shipping = 0
            book_cost = 0
            total_book_cost = 0
            
        #calculate and show total cost based on availability and publisher
        elif cost_type == 3:
            publisher_name = input("Please enter the name of the publisher: ")
            
            for author, publisher, cost, shipping_cost, availability in bdata.itertuples(index=False):
                if publisher_name == publisher:
                    if availability:
                        book_cost += cost
                        book_shipping += shipping_cost
                        temp_total_cost = cost + shipping_cost
                        total_book_cost += temp_total_cost
                
            print("The cost of all available books is:",book_cost,"€, with shipping cost:",book_shipping,"€")
            print("Total cost:",total_book_cost,"€")
            #reset values
            book_shipping = 0
            book_cost = 0
            total_book_cost = 0
        
        else:
            break

"""CASE 10"""
def generateGraph(user_df, books_df):
    menu = 1
        
    while not menu == 0:
        print("\nGRAPH MENU:\n")
        print("1. Number of books per publisher (with copies).")
        print("2. Number of books per publisher.")
        print("3. Number of books per author (with copies).")
        print("4. Number of books per author.")
        print("5. Number of books per category.")
        print("6. Number of books per category (with copies).")
        print("7. Number of books per bookstore (with copies).")
        print("8. Cost of available books.")
        print("9. Number of users per city.")
        print("0. To exit.")
            
        menu = int(input("-> "))
        
        if menu == 1:
            #creating the lists that will be used for the plot
            publisher_list = []
            book_list = []
            #creating data frame
            bdata = books_df.loc[:,["id", "publisher", "copies"]]
            
            #appending the publishers to a list (unique entry)
            for ID, publisher, copies in bdata.itertuples(index=False):
                if publisher not in publisher_list:
                    publisher_list.append(publisher)
                
            #initiating second list
            for book in range(0, len(publisher_list)):
                book_list.append(0)
            
            #getting publisher index from the list for each publisher and adding the copies to the same index for the book list
            for ID, publisher, copies in bdata.itertuples(index=False):
                publisher_index = publisher_list.index(publisher)
                book_list[publisher_index] += copies
            
            #making a horizontal bar graph with matplotlib
            #getting the coordinates of the y bars
            y_pos = np.arange(len(publisher_list))
            plt.barh(y_pos, book_list)
            #annotate y axis
            plt.yticks(y_pos, publisher_list)
            plt.title("Number of books per publisher (with copies).")
            #show graph
            plt.show()
            
        elif menu == 2:
            #creating the lists that will be used for the plot
            publisher_list = []
            book_list = []
            #creating data frame
            bdata = books_df.loc[:,["id", "publisher"]]
            
            #appending the publishers to a list (unique entry)
            for ID, publisher in bdata.itertuples(index=False):
                if publisher not in publisher_list:
                    publisher_list.append(publisher)
                
            #initiating second list
            for book in range(0, len(publisher_list)):
                book_list.append(0)
            
            #getting publisher index from the list for each publisher and adding 1 to the same index for the book list
            for ID, publisher in bdata.itertuples(index=False):
                publisher_index = publisher_list.index(publisher)
                book_list[publisher_index] += 1
            
            #making a horizontal bar graph with matplotlib
            #getting the coordinates of the y bars
            y_pos = np.arange(len(publisher_list))
            plt.barh(y_pos, book_list)
            #annotate y axis
            plt.yticks(y_pos, publisher_list)
            plt.title("Number of books per publisher.")
            #show graph
            plt.show()
            
        elif menu == 3:
            #creating the lists that will be used for the plot
            author_list = []
            book_list = []
            #creating data frame
            bdata = books_df.loc[:,["id", "author", "copies"]]
            
            #appending the authors to a list (unique entry)
            for ID, author, copies in bdata.itertuples(index=False):
                if author not in author_list:
                    author_list.append(author)
                
            #initiating second list
            for book in range(0, len(author_list)):
                book_list.append(0)
            
            #getting author index from the list for each author and adding the copies to the same index for the book list
            for ID, author, copies in bdata.itertuples(index=False):
                author_index = author_list.index(author)
                book_list[author_index] += copies
            
            #making a horizontal bar graph with matplotlib
            #getting the coordinates of the y bars
            y_pos = np.arange(len(author_list))
            plt.barh(y_pos, book_list)
            #annotate y axis
            plt.yticks(y_pos, author_list)
            plt.title("Number of books per author (with copies).")
            #show graph
            plt.show()
            
        elif menu == 4:
            #creating the lists that will be used for the plot
            author_list = []
            book_list = []
            #creating data frame
            bdata = books_df.loc[:,["id", "author"]]
            
            #appending the authors to a list (unique entry)
            for ID, author in bdata.itertuples(index=False):
                if author not in author_list:
                    author_list.append(author)
                
            #initiating second list
            for book in range(0, len(author_list)):
                book_list.append(0)
            
            #getting author index from the list for each author and adding +1 to the same index for the book list
            for ID, author in bdata.itertuples(index=False):
                author_index = author_list.index(author)
                book_list[author_index] += 1
                
            #making a horizontal bar graph with matplotlib
            #getting the coordinates of the y bars
            y_pos = np.arange(len(author_list))
            plt.barh(y_pos, book_list)
            #annotate y axis
            plt.yticks(y_pos, author_list)
            plt.title("Number of books per author.")
            #show graph
            plt.show()
            
        elif menu == 5:
            #creating the lists that will be used for the plot
            categories_list = []
            book_list = []
            #creating data frame
            bdata = books_df.loc[:,["id", "categories"]]
            
            #appending the categories to a list (unique entry)
            for ID, categories in bdata.itertuples(index=False):
                categories = ast.literal_eval(str(categories))
                for category in categories:
                    if category not in categories_list:
                        categories_list.append(category)
                
            #initiating second list
            for book in range(0, len(categories_list)):
                book_list.append(0)
            
            #getting category index from the list for each category and adding +1 to the same index for the book list
            for ID, categories in bdata.itertuples(index=False):
                categories = ast.literal_eval(str(categories))
                for category in categories:
                    category_index = categories_list.index(category)
                    book_list[category_index] += 1
    
            #making a horizontal bar graph with matplotlib
            #getting the coordinates of the y bars
            y_pos = np.arange(len(categories_list))
            plt.barh(y_pos, book_list)
            #annotate y axis
            plt.yticks(y_pos, categories_list)
            plt.title("Number of books per category.")
            #show graph
            plt.show()
            
        elif menu == 6:
            
            #creating the lists that will be used for the plot
            categories_list = []
            book_list = []
            #creating data frame
            bdata = books_df.loc[:,["id", "categories", "copies"]]
            
            #appending the categories to a list (unique entry)
            for ID, categories, copies in bdata.itertuples(index=False):
                categories = ast.literal_eval(str(categories))
                for category in categories:
                    if category not in categories_list:
                        categories_list.append(category)
                
            #initiating second list
            for book in range(0, len(categories_list)):
                book_list.append(0)
            
            #getting category index from the list for each category and adding the copies to the same index for the book list
            for ID, categories, copies in bdata.itertuples(index=False):
                categories = ast.literal_eval(str(categories))
                for category in categories:
                    category_index = categories_list.index(category)
                    book_list[category_index] += copies
                
            #making a horizontal bar graph with matplotlib
            #getting the coordinates of the y bars
            y_pos = np.arange(len(categories_list))
            plt.barh(y_pos, book_list)
            #annotate y axis
            plt.yticks(y_pos, categories_list)
            plt.title("Number of books per category (with copies).")
            #show graph
            plt.show()
            
        elif menu == 7:
            #creating the lists that will be used for the plot
            bookstore_id = []
            book_list = []
            #creating data frame
            bdata = books_df.loc[:,["id", "bookstores"]]
            
            #appending the bookstore id's to a list (unique entry)
            for ID, bookstores in bdata.itertuples(index=False):
                bookstores = ast.literal_eval(str(bookstores))
                bookstores_list = list(bookstores.keys())
                for bookstore in bookstores_list:
                    if bookstore not in bookstore_id:
                        bookstore_id.append(bookstore)
            
            #initiating second list
            for book in range(0, len(bookstore_id)):
                book_list.append(0)
            
            #getting boostore index from the list for each bookstore and adding the copies (values) to the same index for the book list
            for ID, bookstores in bdata.itertuples(index=False):
                bookstores = ast.literal_eval(str(bookstores))
                for key, value in bookstores.items():
                    bookstore_index = bookstore_id.index(key)
                    book_list[bookstore_index] += value
            
            #making a horizontal bar graph with matplotlib
            #getting the coordinates of the y bars
            y_pos = np.arange(len(bookstore_id))
            plt.barh(y_pos, book_list)
            #annotate y axis
            plt.yticks(y_pos, bookstore_id)
            plt.ylabel("Bookstore ID's")
            plt.title("Number of books per bookstore (with copies).")
            #show graph
            plt.show()
            
        
        elif menu == 8:
            #creating the lists that will be used for the plot
            id_list = []
            cost_list = []
            #creating data frame
            bdata = books_df.loc[:,["id", "cost", "shipping_cost", "availability"]]
            
            #appending the book id's to a list (unique entry)
            for ID, cost, shipping_cost, availability in bdata.itertuples(index=False):
                if availability:
                    id_list.append(ID)
                    total_cost = cost + shipping_cost
                    cost_list.append(total_cost)
            
            plt.plot(id_list, cost_list, label = "cost")
            #difine axis names
            plt.xlabel("Book ID's")
            plt.ylabel("Book Cost (€)")
            plt.title("Cost of available books.")
            #show legends
            plt.legend()
            plt.show()
            
        elif menu == 9:
            #creating the lists that will be used for the plot
            cities_list = []
            user_no_list = []
            #creating data frame
            udata = user_df.loc[:,["username", "city"]]
            
            #appending the cities to a list (unique entry)
            for username, city in udata.itertuples(index=False):
                if city not in cities_list:
                    cities_list.append(city)
                
            #initiating second list
            for user in range(0, len(cities_list)):
                user_no_list.append(0)
            
            #getting city index from the list for each city and adding 1 to the same index for each user in the user list
            for username, city in udata.itertuples(index=False):
                cities_index = cities_list.index(city)
                user_no_list[cities_index] += 1
            
            #making a horizontal bar graph with matplotlib
            #getting the coordinates of the y bars
            y_pos = np.arange(len(cities_list))
            plt.barh(y_pos, user_no_list)
            #annotate y axis
            plt.yticks(y_pos, cities_list)
            plt.title("Number users per city.")
            #show graph
            plt.show()
            
        elif menu == 0:
            break
        
        else:
            print("Incorrect input...")

"""CASE 11"""
def deleteUser(user_df):
    udata = user_df.loc[:,["id", "username"]]
    name_exists = 0
    
    #show list of users
    print("\nList of users:")
    for ID, username in udata.itertuples(index=False):
        print("ID:",ID,"| User:",username)
    
    delete_user = input("Enter the username of the user you wish to delete from the data frame: ")
    
    #get index and delete user if possible
    for ID, username in udata.itertuples(index=False):
        if username == delete_user:
            #getting index in form of list and saving it as an integer
            i = user_df.index[user_df["username"] == delete_user].tolist()
            index = i[0]
            #droping the row at the index of the book
            user_df = user_df.drop(index)
                
            print("User deleted successfully!")    
            
            name_exists = 1
            
    if name_exists == 0:
        print("The username you entered doesn't exist in the data frame.")
        
    return user_df

"""CASE 12"""
def deleteComment(books_df):
    #Create data frame
    bdata = books_df.loc[:,["title", "rating"]]
    correct_book = 0
    
    while correct_book == 0:
        edit_title = input("Enter the title of the book you wish to delete the comment of: ")
        name_exists = 0
        found = 0
        
        for title, rating in bdata.itertuples(index=False):
            if edit_title == title:
                #getting index in form of list and saving it as an integer
                i = books_df.index[books_df["title"] == edit_title].tolist()
                index = i[0]
                
                #making the conversion from json str to dict
                converted_rating = ast.literal_eval(str(rating))
                #printing the comments on the book
                for key,value in converted_rating.items():
                    print("User",key,"made this comment:",value)
                
                delete_comment = input("-Enter the name of the user who's comment you wish to delete: ")
                
                for key, value in converted_rating.items():
                    if delete_comment == key:
                        found = 1
                        
                if found == 1:
                    converted_rating.pop(delete_comment)
                    #Rewriting the entry with the new value
                    books_df.at[index, "rating"] = converted_rating
                    print("Comment deleted successfully!")
                else:
                    print("Incorrect username, resuming without changes...")
                
                name_exists = 1
        
        if name_exists == 1:
            correct_book = 1
        else: 
            print("The book does not exist in the data frame.")
            
    return books_df