### DAY 43: Build a Hotel Booking App in OOP Style with Python(Part 3)

Today, I continued to build on my understanding of OOP by learning and practicing more concepts of OOP with the Hotel Booking App codebase.

Recap on what I did yesterday. I had two data sources the cards csv file and card security csv file these contained dummy credit card info and credentials. I used pandas to read both files and saved them in variables. I wrote two classes, CreditCard class and SecureCreditCard class. So this is how these new classes and methods fit into the code logic we had so far. If the hotel is available then we instantiate the SecureCreditCard class since its inheriting the CreditCard class. Then the app checks if the credit card details provided by the user is valid by calling the validate method and if its valid then the app checks if the password the user provided is correct by calling the authenticate method if the credentials is correct the the app books the hotel and generates the Reservation ticket. If at any step the info is wrong we print a message to the user to try again. The app run like it was supposed to after a few tests.

Today, I used the hotel booking app code base to practice more concepts of OOP. I learn about the Class Attributes(class variables and class methods) and Instance Attributes(instance variables and instance methods). I also learnt other concepts like Properties, Static Methods, Magic Methods, Abstract Classes and Abstract Methods.

Day 43 was good, I am learning more and more each day.
