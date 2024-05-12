"""CSV GENERATOR"""
#Generates the necessary csv files at the start of the program if necessary.

import os.path
import pandas as pd

def create_CSV():
    filename_1 = 'user.csv'
    filename_2 = 'admin.csv'    
    filename_3 = 'books.csv'
    
    if not os.path.exists(filename_1):
        
        header = ['id', 'username', 'password', 'address', 'city', 'orders', 'favorites', 'balance']
        data = [[10,'Alex', 'felina@19', 'Roseburn', 'Edinburgh', [142, 132], [106, 141, 107, 108], 180.0], 
                [11,'Nick', '2118159!', 'Krustallophghs 4', 'Lamia', [115, 141], [101, 102, 103, 104, 105, 139], 100.0],
                [12,'Alexandros', '1617#2198', 'Miaoulh 10', 'Athens', [149, 150], [117, 130, 144], 50.0],
                [13,'Irene', '!vidi1234', 'Miaoulh 10', 'Athens', [112, 113], [116], 180.0],
                [14,'Panos', 'Koump7#4321', 'Amarousiou 24', 'Athens', [133, 134, 135], [120, 123, 124, 105], 80.0]]
        
        pd_user = pd.DataFrame(data, columns=header)
        
        #opening the file in write mode
        with open(filename_1, 'w', newline=""):
            pd_user.to_csv(filename_1, index=False)
            
            
    if not os.path.exists(filename_2): 
       
        header = ['id', 'username', 'password', 'bookstores']
        admin1 = [1, 2, 5]
        admin2 = [3, 4, 5]
        data = [[50, 'Nicholaos', '01225@52210', admin1],
                [51, 'Jeremy', '@522101225', admin2]]
        
        pd_admin = pd.DataFrame(data, columns=header)
        
        #opening the file in write mode
        with open(filename_2, 'w', newline=""):
            pd_admin.to_csv(filename_2, index=False)
            
        
    if not os.path.exists(filename_3): 
        
        header = ['id', 'title', 'author', 'publisher', 'categories', 'cost', 'shipping_cost', 'availability', 'copies', 'bookstores', 'rating']
        data = [[101, 'Percy Jackson and the Olympians: The lightning thief', 'Rick Riordan', 'Disney Hyperion', ['Fantasy'], 20.0, 2.25, True, 21, {1: 10, 2: 3, 5: 8}, None], 
                [102, 'Percy Jackson and the Olympians: The Sea of Monsters', 'Rick Riordan', 'Disney Hyperion', ['Fantasy'], 22.3, 2.25, True, 18, {1: 10, 2: 3, 5: 5}, None],
                [103, 'Percy Jackson and the Olympians: The Titans Curse', 'Rick Riordan', 'Disney Hyperion', ['Fantasy'], 23.4, 2.25, True, 9, {2: 3, 5: 6}, None],
                [104, 'Percy Jackson and the Olympians: The Battle of the Labyrinth', 'Rick Riordan', 'Disney Hyperion', ['Fantasy'], 20.0, 2.25, True, 12, {1: 2, 2: 3, 5: 20}, None],
                [105, 'Percy Jackson and the Olympians: The Last Olympian', 'Rick Riordan', 'Disney Hyperion', ['Fantasy'], 25.5, 2.25, True, 21, {1: 10, 2: 3, 5: 8}, {'Nick':'4, Overwhelming finale to an amazing series!'}],
                
                [106, 'The Lord of the Rings: The fellowship of the Ring', 'J.R.R Tolkien', 'Allen & Unwin', ['Fantasy', 'Adventure'], 20.0, 2.25, True, 21, {3: 10, 4: 3, 5: 8}, None],
                [107, 'The Lord of the Rings: The Two Towers', 'J.R.R Tolkien', 'Allen & Unwin', ['Fantasy', 'Adventure'], 22.3, 3, True, 18, {1: 10, 2: 3, 5: 5}, None],
                [108, 'The Lord of the Rings: The Return of the King', 'J.R.R Tolkien', 'Allen & Unwin', ['Fantasy', 'Adventure'], 25.5, 1.5, True, 30, {1: 10, 3: 3, 4: 17}, None],
                [109, 'The Hobbit', 'J.R.R Tolkien', 'Allen & Unwin', ['Fantasy', 'Adventure'], 15.0, 2.25, False, 0, {1: 0, 2: 0, 5: 0}, None],
                
                [110, 'Harry Potter and the Philosophers stone', 'J.K Rowling', 'Bloomsbury Publishing', ['Fantasy'], 10.0, 4.0, True, 21, {1: 10, 2: 3, 5: 8}, None],
                [111, 'Harry Potter and the Chamber of Secrets', 'J.K Rowling', 'Bloomsbury Publishing', ['Fantasy'], 10.0, 4.0, True, 30, {1: 10, 2: 3, 5: 17}, None],
                [112, 'Harry Potter and the Prisoner of Azkaban', 'J.K Rowling', 'Bloomsbury Publishing', ['Fantasy'], 10.0, 4.0, True, 10, {1: 1, 2: 3, 3: 1, 4: 4, 5:1}, None],
                [113, 'Harry Potter and the Goblet of fire', 'J.K Rowling', 'Bloomsbury Publishing', ['Fantasy'], 10.0, 4.0, False, 0, {1: 0, 2:0, 3: 0, 5: 0}, None],
                [114, 'Harry Potter and the Order of the Phoenix', 'J.K Rowling', 'Bloomsbury Publishing', ['Fantasy'], 12.5, 4.0, True, 18, {4: 10, 5: 8}, None],
                [115, 'Harry Potter and the Half-Blood Prince', 'J.K Rowling', 'Bloomsbury Publishing', ['Fantasy'], 12.5, 4.0, True, 3, {1: 1, 5: 2}, None],
                [116, 'Harry Potter and the Deathly Hallows', 'J.K Rowling', 'Bloomsbury Publishing', ['Fantasy'], 13.0, 3.0, True, 42, {2: 10, 3: 26, 4: 6}, None],
                
                [117, 'A tale of Two Cities: Book the First', 'Charles Dickens', 'Chapman & Hall', ['Historical'], 12.25, 2.25, True, 14, {1: 10, 2: 3, 5: 1}, None],
                [118, 'A tale of Two Cities: Book the Second', 'Charles Dickens', 'Chapman & Hall', ['Historical'], 12.25, 2.25, True, 18, {2: 6, 3: 10, 4: 2}, None],
                [119, 'A tale of Two Cities: Book the Third', 'Charles Dickens', 'Chapman & Hall', ['Historical'], 12.25, 2.25, True, 11, {1: 5, 4: 6}, None],
                
                [120, 'A Game of Thrones', 'George R.R. Martin', 'Bantam Books', ['Fantasy'], 14.0, 2.25, True, 14, {1: 10, 2: 3, 5: 1}, None],
                [121, 'A Clash of Kings', 'George R.R. Martin', 'Bantam Books', ['Fantasy'], 14.0, 2.25, True, 14, {1: 8, 3: 3, 4: 3}, None],
                [122, 'A Storm of Swords', 'George R.R. Martin', 'Bantam Books', ['Fantasy'], 14.0, 2.25, True, 15, {2: 10, 4: 5}, None],
                [123, 'A Feast for Crows', 'George R.R. Martin', 'Bantam Books', ['Fantasy'], 15.0, 2.25, True, 40, {1: 10, 2: 22, 3: 8}, None],
                [124, 'A Dance with Dragons', 'George R.R. Martin', 'Bantam Books', ['Fantasy'], 20.0, 2.25, True, 10, {1: 5, 2: 5}, None],
                [125, 'The Winds of Winter', 'George R.R. Martin', 'Bantam Books', ['Fantasy'], 20.0, 2.25, False, 0, {1: 0, 2: 0, 3: 0, 4: 0, 5: 8}, {'Panos': '0, Still waiting.....'}],
                
                [126, 'City of Bones', 'Cassandra Clare', 'Margaret K. McElderry', ['Paranormal'], 20.0, 2.25, True, 21, {1: 10, 2: 3, 5: 8}, None], 
                [127, 'City of Ashes', 'Cassandra Clare', 'Margaret K. McElderry', ['Paranormal'], 22.3, 2.25, True, 18, {1: 10, 2: 3, 5: 5}, None],
                [128, 'City of Glass', 'Cassandra Clare', 'Margaret K. McElderry', ['Paranormal'], 23.4, 2.25, True, 9, {2: 3, 5: 6}, None],
                [129, 'City of Fallen Angels', 'Cassandra Clare', 'Margaret K. McElderry', ['Paranormal'], 20.0, 2.25, True, 12, {1: 2, 2: 3, 5: 20}, None],
                [130, 'City of Lost Souls', 'Cassandra Clare', 'Margaret K. McElderry', ['Paranormal'], 25.5, 2.25, True, 21, {1: 10, 2: 3, 5: 8}, None],
                [131, 'City of Heavenly Fire', 'Cassandra Clare', 'Margaret K. McElderry', ['Paranormal'], 20.0, 2.25, True, 21, {3: 10, 4: 3, 5: 8}, None],
                
                [132, 'The Gunslinger', 'Stephen King', 'Grant', ['Science Fiction','Fantasy'], 22.3, 3, True, 18, {1: 10, 2: 3, 5: 5}, None],
                [133, 'The Drawing of the Three', 'Stephen King', 'Grant', ['Science Fiction','Fantasy'], 25.5, 1.5, True, 30, {1: 10, 3: 3, 4: 17}, None],
                [134, 'The Waste Lands', 'Stephen King', 'Grant', ['Science Fiction','Fantasy'], 15.0, 2.25, False, 0, {1: 0, 2: 0, 5: 0}, None],
                [135, 'Wizard and Glass', 'Stephen King', 'Grant', ['Science Fiction','Fantasy'], 10.0, 4.0, True, 21, {1: 10, 2: 3, 5: 8}, None],
                [136, 'The Litle Sisters of Eluria', 'Stephen King', 'Grant', ['Science Fiction','Fantasy'], 10.0, 4.0, True, 30, {1: 10, 2: 3, 5: 17}, None],
                [137, 'Wolves of the Calla', 'Stephen King', 'Grant', ['Science Fiction','Fantasy'], 10.0, 4.0, True, 10, {1: 1, 2: 3, 3: 1, 4: 4, 5:1}, None],
                [138, 'Song of Susannah', 'Stephen King', 'Grant', ['Science Fiction','Fantasy'], 10.0, 4.0, False, 0, {1: 0, 2:0, 3: 0, 5: 0}, None],
                [139, 'The Dark Tower', 'Stephen King', 'Grant', ['Science Fiction','Fantasy'], 12.5, 4.0, True, 18, {4: 10, 5: 8}, None],
                [140, 'The Wind Through the Keyhole', 'Stephen King', 'Grant', ['Science Fiction','Fantasy'], 12.5, 4.0, True, 3, {1: 1, 5: 2}, None],
                
                [141, 'Around the World in Eighty Days', 'Jules Verne', 'Pierre-Jules Hetzel', ['Adventure'], 13.0, 3.0, True, 42, {2: 10, 3: 26, 4: 6}, {'Alex': '5, What an amazing journey!'}],
                [142, 'From the Earth to the Moon', 'Jules Verne', 'Pierre-Jules Hetzel', ['Science Fiction'], 12.25, 2.25, True, 14, {1: 10, 2: 3, 5: 1}, None],
                [143, 'Journey to the Center of the Earth', 'Jules Verne', 'Pierre-Jules Hetzel', ['Adventure', 'Science Fiction'], 12.25, 2.25, True, 18, {2: 6, 3: 10, 4: 2}, None],
                [144, 'Twenty Thousand Leagues Under the Sea', 'Jules Verne', 'Pierre-Jules Hetzel', ['Adventure'], 12.25, 2.25, True, 11, {1: 5, 4: 6}, None],
                
                [145, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 'HarperCollins', ['Fantasy'], 14.0, 2.25, True, 14, {1: 10, 2: 3, 5: 1}, None],
                [146, 'Price Caspian', 'C.S. Lewis', 'HarperCollins', ['Fantasy'], 14.0, 2.25, True, 14, {1: 8, 3: 3, 4: 3}, None],
                [147, 'The Voyage of the Dawn Treader', 'C.S. Lewis', 'HarperCollins', ['Fantasy'], 14.0, 2.25, True, 15, {2: 10, 4: 5}, None],
                [148, 'The Siler Chair', 'C.S. Lewis', 'HarperCollins', ['Fantasy'], 15.0, 2.25, True, 40, {1: 10, 2: 22, 3: 8}, None],
                [149, 'The Horse and His Boy', 'C.S. Lewis', 'HarperCollins', ['Fantasy'], 20.0, 2.25, True, 10, {1: 5, 2: 5}, None],
                [150, 'The Magicians Nephew', 'C.S. Lewis', 'HarperCollins', ['Fantasy'], 20.0, 2.25, False, 0, {1: 0, 2: 0, 3: 0, 4: 0, 5: 8}, None],
                [151, 'The Last Battle', 'C.S. Lewis', 'HarperCollins', ['Fantasy'], 12.5, 4.0, True, 18, {4: 10, 5: 8}, None],
                [152, 'The Last last Battle', 'C.S. Lewis', 'HarperCollins', ['Fantasy'], 13.0, 4.0, True, 10, {4: 5, 5: 5}, None]]
        
        pd_books = pd.DataFrame(data, columns=header)
        
        #opening the file in write mode
        with open(filename_3, 'w', newline=""):
            pd_books.to_csv(filename_3, index=False)