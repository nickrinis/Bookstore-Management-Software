"""USER USE CASES"""
import sys
import ast
import random
import math

"""CASE 1"""
def csvEntry(user_df, books_df, logged_in):
    #creating data frames
    udata = user_df.loc[:,["id", "favorites"]]
    bdata = books_df.loc[:,["id", "title", "availability"]]
    success = 0
    
    for ID, favorites in udata.itertuples(index=False):
        if ID==logged_in:
            #getting index in form of list and saving it as an integer
            i = user_df.index[user_df["id"] == logged_in].tolist()
            index = i[0]
            #converting favorites
            favorites = ast.literal_eval(str(favorites))
            
            loops = int(input("Please enter the ammount of entries you would like to add to your favorites: "))
            #loop for all the entries
            for number in range(0, loops):
                correct_book = 0
                while correct_book == 0:
                    name_exists = 0
                    
                    book_title = input("-Enter the title of the book you wish to add to your favorites: ")
                    for ID, title, availability in bdata.itertuples(index=False):
                        if book_title == title:
                            #checking if the ID is already in the list
                            if ID in favorites:
                                print("The book is already in your favorites!")
                            else:
                                favorites.append(ID)
                                success = 1
                            name_exists = 1
                        
                    if name_exists == 1:
                        correct_book = 1
                    else: 
                        print("The book does not exist in the data frame.")
            
            #saving the new favorite values to user_df
            user_df.at[index, "favorites"] = favorites
            
            #Reloading the csv file
            with open("user.csv", 'w', newline=""):
                user_df.to_csv("user.csv", index=False)
            
            if success == 1:
                print("Changes loaded successfully!")
    
"""CASE 2"""
def singleEntry(user_df, books_df, logged_in):
    #creating data frames
    udata = user_df.loc[:,["id", "favorites"]]
    bdata = books_df.loc[:,["id", "title", "availability"]]
    success = 0
    correct_book = 0
    
    for ID, favorites in udata.itertuples(index=False):
        if ID==logged_in:
            #getting index in form of list and saving it as an integer
            i = user_df.index[user_df["id"] == logged_in].tolist()
            index = i[0]
            #converting favorites
            favorites = ast.literal_eval(str(favorites))
        
            while correct_book == 0:
                name_exists = 0
                
                book_title = input("-Enter the title of the book you wish to add to your favorites: ")
                for ID, title, availability in bdata.itertuples(index=False):
                    if book_title == title:
                        #checking if the ID is already in the list
                        if ID in favorites:
                            print("The book is already in your favorites!")
                        else:
                            favorites.append(ID)
                            success = 1
                        name_exists = 1
                    
                if name_exists == 1:
                    correct_book = 1
                else: 
                    print("The book does not exist in the data frame.")
        
            #saving the new favorite values to user_df
            user_df.at[index, "favorites"] = favorites
        
    if success == 1:
        print("The book was added to your favorites!")
        
    return user_df
    
"""CASE 3"""
def editData(user_df, logged_in):
    udata = user_df.loc[:,["id", "username", "password", "address", "city", "balance"]]
    udata2 = user_df.loc[:,["id", "username", "password"]]
    correct_username = 0
    correct_password = 0
    containsSpecialCharacter = 0
    passwordLength = 0
    specialCharacters = "!@#$%^&*()-+?_=,<>/"
    
    for ID, username, password, address, city, balance in udata.itertuples(index=False):
        if ID==logged_in:
            #getting index in form of list and saving it as an integer
            i = user_df.index[user_df["id"] == logged_in].tolist()
            index = i[0]
            #Getting data
            
            #username
            while correct_username == 0:
                unique = 1
                new_username = (input("Please enter your new username: "))
                for ID, name, pword in udata2.itertuples(index=False):
                    if new_username == name:
                        unique = 0
                if not unique == 0:
                    correct_username = 1
                else:
                    print("Username is taken, please choose another.")

            #password
            while correct_password == 0:
                unique = 1
                new_password = (input("Please enter your new password: "))
                if any(character in specialCharacters for character in new_password):
                    containsSpecialCharacter = 1
                if len(new_password) >= 8:
                    passwordLength = 1
                
                for ID, name, pword in udata2.itertuples(index=False):
                    if new_password == pword:
                        unique = 0
                if unique == 1 and containsSpecialCharacter == 1 and passwordLength ==1:
                    correct_password = 1
                else:
                    print("Password must be unique, have at least 8 characters and 1 special character, please enter a new password.")
                    
            password_ver = (input("Please enter your password again: "))
            
            if not new_password == password_ver:
                print("Passwords must much! exiting...")
                sys.exit
            else:
                new_address = input("Please enter your new address: ")
                new_city = input("Please enter your new city: ")
                new_balance = float(input("Please enter your balance: "))
                
                #Rewriting the entry with the new values
                user_df.at[index, "username"] = new_username
                user_df.at[index, "password"] = new_password
                user_df.at[index, "address"] = new_address
                user_df.at[index, "city"] = new_city
                user_df.at[index, "balance"] = new_balance
                
                print("Changes made successfully!")
               
    return user_df

"""CASE 4"""
def emptyFavorites(user_df, logged_in):
    udata = user_df.loc[:,["id", "favorites"]]
   
    for ID, favorites in udata.itertuples(index=False):
        if ID==logged_in:
            #getting index in form of list and saving it as an integer
            i = user_df.index[user_df["id"] == logged_in].tolist()
            index = i[0]
            favorites = ast.literal_eval(str(favorites))
            favorites.clear()
            user_df.at[index, "favorites"] = favorites
            
            print("Favorites list emptied successfully!")
            
    return user_df

"""CASE 5"""
def checkBalance(user_df, logged_in):
    udata = user_df.loc[:,["id", "balance"]]
    #printing the balance
    for ID, balance in udata.itertuples(index=False):
        if ID==logged_in:
            print("Your remaining balance is:",balance,"€")

"""CASE 6"""
def checkBookAvail(user_df, books_df, logged_in):
    udata = user_df.loc[:,["id", "favorites"]]
    bdata = books_df.loc[:,["id", "title", "cost", "shipping_cost", "availability"]]
    
    for ID, favorites in udata.itertuples(index=False):
        if ID==logged_in:
            favorites = ast.literal_eval(str(favorites))
            print("\n-Enter 1 if you wish to see the availability and price of certain books in your favorites list.")
            print("-Enter 2 if you wish to see the availability and price of all the books in your favorites list.")
            options = int(input("-> "))
            
            #printing the availability and cost of certain books through a temp list
            if options == 1:
                print("Your favorites list:",favorites)
                
                list_length = int(input("Enter the amount of books that you wish to check the availability and cost of:"))
                temp_list = []
                for number in range(0,list_length):
                    book_id = int(input("Enter the ID of the book: "))
                    temp_list.append(book_id)
                
                for ID, title, cost, shipping_cost, availability in bdata.itertuples(index=False):
                    if ID in temp_list:
                        if availability:
                            print("Book:",title,", is available with a cost of",cost,"€ and shipping cost",shipping_cost,"€")
                            total_cost = cost + shipping_cost
                            print("Total cost:",total_cost,"€\n")
                        else:
                            print("Book:",title,", is not available")
                            
            #printing the availability and cost of all the books in the favorites list
            elif options == 2:
                for ID, title, cost, shipping_cost, availability in bdata.itertuples(index=False):
                    if ID in favorites:
                        if availability:
                            print("Book:",title,", is available with a cost of",cost,"€ and shipping cost",shipping_cost,"€")
                            total_cost = cost + shipping_cost
                            print("Total cost:",total_cost,"€\n")
                        else:
                            print("Book:",title,", is not available")
            else:
                print("Incorrect input...")
            
"""CASE 7"""
def checkOrders(user_df, books_df, logged_in):
    udata = user_df.loc[:,["id", "orders"]]
    bdata = books_df.loc[:,["id", "title"]]
    
    for ID, orders in udata.itertuples(index=False):
        if ID==logged_in:
            orders = ast.literal_eval(str(orders))
            print("Your orders are:")
            #printing the id and title for each book in the orders list
            for ID, title in bdata.itertuples(index=False):
                if ID in orders:
                    print("-ID:",ID," | Title:",title)
                
"""CASE 8"""
def editOrders(user_df, books_df, logged_in):
    udata = user_df.loc[:,["id", "orders", "balance"]]
    bdata = books_df.loc[:,["id", "title", "cost", "shipping_cost", "availability", "copies", "bookstores"]]
    correct_book = 0
    book_cost = 0
    
    for ID, orders, balance in udata.itertuples(index=False):
        if ID==logged_in:
            #user index
            j = user_df.index[user_df["id"] == logged_in].tolist()
            user_index = j[0]
            
            #converting the orders variable 
            converted_orders = ast.literal_eval(str(orders))
            
            print("\n-Enter 1 if you wish to add a book to your orders.")
            print("-Enter 2 if you wish remove a book from your orders.")
            options = int(input("-> "))
            
            if options == 1:
                while correct_book == 0:
                    name_exists = 0
                    book_title = input("Please enter the title of the book you wish to order: ")
                    for ID, title, cost, shipping_cost, availability, copies, bookstores in bdata.itertuples(index=False):
                        if book_title == title:
                            #book index
                            i = books_df.index[books_df["title"] == book_title].tolist()
                            book_index = i[0]
                            
                            converted_bookstores = ast.literal_eval(str(bookstores))
                            book_cost = cost + shipping_cost
                            
                            if copies >= 1:
                                if balance >= book_cost:
                                    for key, value in converted_bookstores.items():
                                        print("Bookstore: ",key, " has copies",value)
                                    
                                    selection = int(input("Please select which bookstore you want to order from: "))
                                    
                                    if converted_bookstores[selection] == 0:
                                        print("This bookstore doesn't have any copies left, we apologize for the inconvenience.")
                                    else:
                                        #changes on the user data frame
                                        converted_orders.append(ID)
                                        balance = balance - book_cost
                                        user_df.at[user_index, "orders"] = converted_orders
                                        user_df.at[user_index, "balance"] = balance
                                        
                                        #changes on the books data frame
                                        copies = copies - 1
                                        if copies == 0:
                                            availability = False
                                            books_df.at[book_index, "availability"] = availability
                                            
                                        converted_bookstores[selection] = converted_bookstores[selection] - 1
                                        books_df.at[book_index, "copies"] = copies
                                        books_df.at[book_index, "bookstores"] = converted_bookstores
                                        
                                        print("Book successfully added to your orders!")
                                else:
                                    print("Your balance is not enough to order this book.")
                            else:
                                print("This book is no longer available, we apologize for the inconvenience.")
                                availability = False
                                books_df.at[book_index, "availability"] = availability
                            
                            name_exists = 1
                            
                    if name_exists == 1:
                        correct_book = 1
                    else: 
                        print("The book does not exist in the data frame.")
                            
            elif options == 2:
                print("Your orders are: ")
                for IDb, title, cost, shipping_cost, availability, copies, bookstores in bdata.itertuples(index=False):
                    if IDb in orders:
                        print("-",title)
                
                while correct_book == 0:
                    name_exists = 0
                    book_title = input("Please enter the title of the book you wish to remove from your orders: ")
                    for ID, title, cost, shipping_cost, availability, copies, bookstores in bdata.itertuples(index=False):
                        if book_title == title:
                            if ID in converted_orders:
                                #book index
                                i = books_df.index[books_df["title"] == book_title].tolist()
                                book_index = i[0]
                            
                                converted_bookstores = ast.literal_eval(str(bookstores))
                                book_cost = cost + shipping_cost
                            
                                for key, value in converted_bookstores.items():
                                    print("Bookstore: ",key)
                                    
                                selection = int(input("Please select which bookstore you want to cancel the order from: "))
                                    
                                if copies == 0:
                                    availability = True
                                    books_df.at[book_index, "availability"] = availability
                            
                                #changes on the user data frame
                                converted_orders.remove(ID)
                                balance = balance + book_cost
                                user_df.at[user_index, "orders"] = converted_orders
                                user_df.at[user_index, "balance"] = balance
                            
                                #changes on the books data frame
                                copies = copies + 1
                                converted_bookstores[selection] = converted_bookstores[selection] + 1
                                books_df.at[book_index, "copies"] = copies
                                books_df.at[book_index, "bookstores"] = converted_bookstores
                                        
                                print("Book successfully removed from your orders!")
                            else:
                                print("The book doesn't exist in your orders...")
                                
                            name_exists = 1
                            
                    if name_exists == 1:
                        correct_book = 1
                    else: 
                        print("The book does not exist in the data frame.")
                
            else:
                print("Incorrect input...")
            
    return user_df, books_df

"""CASE 9"""
def checkCopies(user_df, books_df, logged_in):
    #creating data frames
    udata = user_df.loc[:,["id", "balance"]]
    bdata = books_df.loc[:,["id", "title", "cost", "shipping_cost", "availability", "copies"]]
    correct_book = 0
    
    for ID, balance in udata.itertuples(index=False):
        if ID==logged_in:
           while correct_book == 0:
               name_exists = 0
               
               book_title = input("-Enter the title of the book you wish to check the ammount of copies you can purchase: ")
               for ID, title, cost, shipping_cost, availability, copies in bdata.itertuples(index=False):
                   #if it exists and if available, get total cost and declare basket and copy number
                   if book_title == title:
                       if availability:
                          book_cost = cost + shipping_cost
                          basket = 0
                          return_copies = 0
                          #while our basket + the would be added copy is less or equal to the balance and the copy number does not exceed the book copies
                          while (basket + book_cost <= balance) and (return_copies + 1 < copies):
                             #add to the variable that will be shown to the user
                             return_copies += 1
                             #add to basket for further iterations
                             basket += book_cost
                          
                          print("You can purchase",return_copies,"copies of the book:",title)
                       else:
                           print("This book is not available currently, we apologize for the inconvenience")
                       name_exists = 1
                   
               if name_exists == 1:
                   correct_book = 1
               else: 
                   print("The book does not exist in the data frame.")
       

"""CASE 10"""
def getSuggestions(user_df, books_df, logged_in):
    #initializing the random number generator
    random.seed()
    
    #creating data frames
    udata = user_df.loc[:,["id", "orders", "favorites"]]
    bdata = books_df.loc[:,["id", "title", "categories"]]
    
    #counts for each category
    category_1_count = 0
    category_2_count = 0
    category_3_count = 0
    category_4_count = 0
    category_5_count = 0
    #category with the highest count
    suggestion_Category = 0

    for ID, orders, favorites in udata.itertuples(index=False):
        if ID==logged_in:
            #converting the orders/favorites variables 
            orders = ast.literal_eval(str(orders))
            favorites = ast.literal_eval(str(favorites))

            for ID, title, categories in bdata.itertuples(index=False):
                #for each book in the favorites list find the count per category
                if ID in favorites:
                    if "Fantasy" in categories:
                        category_1_count += 1
                    if "Adventure" in categories:
                        category_2_count += 1
                    if "Historical" in categories:
                        category_3_count += 1
                    if "Paranormal" in categories:
                        category_4_count += 1
                    if "Science Fiction" in categories:
                        category_5_count += 1
                        
            #creating a dictionary with the count num as key and the category as type
            countList = {}
            countList[category_1_count] = "Fantasy"
            countList[category_2_count] = "Adventure"
            countList[category_3_count] = "Historical"
            countList[category_4_count] = "Paranormal"
            countList[category_5_count] = "Science Fiction"
            
            #checking which category has the max number and asigning the chosen category to a variable
            if countList.get(max(countList)) == "Fantasy":
                suggestion_Category = "Fantasy"
            elif countList.get(max(countList)) == "Adventure":
                suggestion_Category = "Adventure"
            elif countList.get(max(countList)) == "Historical":
                suggestion_Category = "Historical"
            elif countList.get(max(countList)) == "Paranormal":
                suggestion_Category = "Paranormal"
            elif countList.get(max(countList)) == "Science Fiction":
                suggestion_Category = "Science Fiction"
                
            suggestion_List = []

            for ID, title, categories in bdata.itertuples(index=False):
                categories = ast.literal_eval(str(categories))
                
                if (ID not in orders) and (ID not in favorites):
                    if suggestion_Category in categories:
                        suggestion_List.append(title)

            #getting the suggestion list length, dividing it by 3 and rounding the number up.
            list_length = len(suggestion_List)
            choice_number = math.ceil((list_length / 3))

            #returns a list as big as the k we define with random choices
            rand_suggestion = random.sample(suggestion_List, k=choice_number)
            print("\nBased on your preferences, you may also like: ")
            for book in rand_suggestion:
                print("-",book)
                
            
"""CASE 11"""
def makeComment(user_df, books_df, logged_in):
    #creating data frames
    udata = user_df.loc[:,["id","username", "orders"]]
    bdata = books_df.loc[:,["id", "title", "rating"]]
    correct_book = 0
    
    for ID, username, orders in udata.itertuples(index=False):
        if ID==logged_in:
            #converting the orders variable 
            converted_orders = ast.literal_eval(str(orders))
            
            print("Your orders are: ")
            for IDb, title, rating, in bdata.itertuples(index=False):
                if IDb in converted_orders:
                    print("-",title)
            
            while correct_book == 0:
                name_exists = 0
               
                book_title = input("-Enter the title of the book you wish to add a comment on: ")
                for ID, title, rating, in bdata.itertuples(index=False):
                    #if it exists and if in orders
                    if book_title == title:
                        if ID in converted_orders:
                            #book index
                            i = books_df.index[books_df["title"] == book_title].tolist()
                            book_index = i[0]
                            
                            #If there is no dictionary in the row, rating = float
                            if type(rating) == float:
                                #Empty dictionary
                                rating = {}
                                score = input("-Enter your score for the book: ")
                                com = input("-Enter your comment for the book (if any): ")
                                comment = score+", "+com
                                
                                rating[username] = comment
                                #storing the new comment dictionary in the data frame
                                books_df.at[book_index, "rating"] = rating
                                
                            else:
                                #converting to a dictionary
                                converted_rating = ast.literal_eval(str(rating))
                                score = input("-Enter your score for the book [0-5]: ")
                                com = input("-Enter your comment for the book (if any): ")
                                comment = score+", "+com
                                
                                converted_rating[username] = comment
                                #storing the new comment dictionary in the data frame
                                books_df.at[book_index, "rating"] = converted_rating
                                
                            print("Comment added successfully!")
                        else:
                            print("This book is not in your orders, unable to make comment.")
                        name_exists = 1
                   
                if name_exists == 1:
                    correct_book = 1
                else: 
                    print("The book does not exist in the data frame.")
    
    return books_df