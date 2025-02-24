### DAY 52: Build a Web App with Django Python (Part 2) 

Today, I continued to work on web development. I started building app 15 which is a Job Application Form built with django.

Recap on what I did yesterday. I added a name parameter to the input elements and created a variable for each input and used the flask request.form method to get the data. I then proceed to add a database to the app to store user data. I imported the flask sqlalchemy module and instantiated the sqlalchemy class with the flask app as a parameter. I created a class Form for the database model where I added my database table schema. I also added a submission notification message to the frontend once the user hits submit. I used jinja2 in the html code to call the flash message from my backend. The last thing I did was add a sending confirmation email functionality after the user submits the form.

Today, I started building a job form application web app with django. I set up a django project and an app in my environment. I also set up the database models and made the database migrations. I created a templates folder to house the html that would be  rendered. Finally, I created a urls.py and edited the views.py in my app directory for the rendering of the html page.


Day 52 was good, I am learning more and more each day. I will continue building the app tomorrow.
