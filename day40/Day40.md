### DAY 40: Introduction to Object-Oriented Programming(OOP) with Python

Today, I learned all about Object-Oriented Programming and converted the code from yesterday from functional programming to OOP.

Recap on what I did yesterday. I moved from file storage to a sqlite3 database. Before I could work with databases, I had to learn about SQL databases and the syntax and how to connect to your database. I created a database and added a table with the fields band,city and date. I changed the code in the data store function to insert the scraped data into the database by the fields in the data. I also changed the code in the read data function to fetch the data from the database based on fields I provided. The app worked after I tested the code and I was able to complete the app. Today, I converted the functional code to OOP. Since I had different functions for different parts of the program, I decided to group the ones that served a similar purpose and put them into classes. I created 3 classes, the scrapper and extraction functions now methods under OOP rules went into the Event class. The email function now send method went into the Email class. The read data and store data functions now methods went into the Database class and I added an init method specifically for the connection to the database. I initialized instances of these classes and called the methods and was able to get the application working just fine. I was able to understand certain concepts in OOP like classes, objects, init and self. I have a bit of a good grasp of OOP as of today.

Also, I did a [side-project](./SP-OOP/) where I completed a set of tasks that helped me understand the concept of Object-Oriented Programming better.

All in all, day 40 was good, I am learning more and more each day.
