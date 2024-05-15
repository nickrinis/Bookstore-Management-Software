<h1 align="center">Bookstore-Management-Software</h1>
<p align="justify"><strong>Simulates online bookstore management through the use of DataFrames. Depending on the currently logged-in user and their access to the system, the software will have a different range of functionalities. It helps administrators efficiently manage their inventory throughout multiple stores as well as manage sales through cost calculation and graphs. Additionally, the software can be used as an account management tool. For users, it allows them to edit their basket and preferences, check the availability of certain books and their balance, receive suggestions, and make comments on a book of their choosing.  </strong>
<br/>
<h2>About</h2>
This project was part of my fourth-year Python course. The grade counted towards my diploma. A lot of thanks to my tutor <a href="https://github.com/anthonydadaliaris" target="_blank">Anthony Dadaliaris</a> who guided me through the whole process and allowed me to upload the project here.

<h2>Installation</h2>

1. Download this project as zip and extract it.
2. Download Python and the necessary libraries (Pandas, NumPy, Matplotlib, etc.).
3. Run Bookstore_Management_Software.py through your IDE of choice.

Alternatively:
1. Clone the repository: git clone https://github.com/nickrinis/Bookstore-Management-Software.git
2. Navigate to the project directory: cd Bookstore-Management-Software
3. Run the main Python script: python Bookstore_Management_Software.py

<h2>Usage</h2>

Once it starts running, the user will be prompted to either log in as an administrator, user or simply create an account. Already existing credentials can be found in the 'csv_generator.py' file under the 'create_CSV()' function. 

Depending on how the user logs in they will be presented with a different menu of functionalities. 
As an administrator, you can:
- Manage customers and inventory.
- Add new books.
- Check the availability of certain books.
- Calculate costs.
- Generate graphs.
- Delete users/comments.

When logged-in as a customer you can:
- Manage your favourites.
- Edit your personal information.
- Check your balance as well as the amount of copies you can purchase of a specific book.
- Manage and see your orders.
- Get book suggestions from the system depending on your activity.
- Write comments about the books.

<h2>Credits</h2>

Bookstore Management Software relies on the following libraries and tools:
- Pandas
- Numpy
- Matplotlib
- Other standard Python libraries


<h2>Contact</h2>
If you have any questions or feedback, please contact me at [nickmarinis12@hotmail.gr](mailto:nickmarinis12@hotmail.gr).

<h2>Copyright</h2>
This project is licensed under the terms of the MIT license.
