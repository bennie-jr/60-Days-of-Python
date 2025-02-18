### DAY 48: Build a MySQL Student Management System with Python

Today, I worked on app number 12 by using a different database service. This is a Student Management System with a MySQL database.

Recap on what I did yesterday. I added a toolbar which acted like a shortcut to things from the menu bar and these were the add student button and search student button, I used images as representation buttons and added a click event which would trigger their functionalities respectively. I also added a status bar which had two buttons, an edit button and a delete button. These two buttons are not visible at first but once a user clicks on any of the rows or columns on the table, these buttons will appear and as the names imply, edit will edit the data of the row you clicked and the delete will delete that row. The edit button when clicked opens a dialog box where you can edit the existing students data and once you update the info the database and table in the gui is updated. For the delete button I added a confirmation dialog box and confirmation message when the user confirms deletion. I also added an About dialog box which shows up when the About button on the menu bar is clicked, the dialog just gives you a brief description on what the app is about.

Today, I just swapped out the SQLite3 database for MySQL database and modified the database connection code to suit what MySQL requires. I installed MySQL and created a database, a table (same table format I used with SQLite3). I inserted data into the table and all I was doing with creating the database and inserting table data was to get familiar with how MySQL works. After I was done creating the database and the table, I modified the codebase to suit MySQL. I added the authentication with the database connection and then edited the SQL queries of SQLite3 to the use case of MySQL. I tested out the code after I was done and everything worked well.

Also I learnt about the differences between MySQL database and SQLite3.

Day 48 was good, I am learning more and more each day.
