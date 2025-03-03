### DAY 55: Build a Food Order Management Web App with Django Python (Part 1) 

Today, I continued to work on web development. I started building app 16 which is a Restaurant Menu Management App built with django.

Recap on what I did yesterday. I created an admin interface for the application. I created a class in the admin.py in my application folder to help me customize the admin interface. I addded search fields, filters, ordering etc to the admin interface. I also created a base template. This base template was for the frontend and this base template is basically to help me not repeat code. I also added a nav bar to the base template html code. The nav bar helps to navigate to the different pages on the webpage without typing in the routes.

Today, I started building the Restaurant Menu Management app. I started by creating a QR Code for the app. I imported the qrcode module and pillow as a dependency. The code for generating the qr code was a simple one liner so it didnt take me very long. Next, I proceed to initialize and set up the Django Project and the app. The last thing I did today was create the database model. I created a class called Items and added the database schema for the table. I also added a User to the table which would serve as a foreign key with a many to one relationship. I then made the database migrations and the table was created out of my defined schema. That's all I did today, I will continue tomorrow but so far so good.

Day 55 was good, I am learning more and more each day. I will continue building the app tomorrow.
