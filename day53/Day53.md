### DAY 53: Build a Web App with Django Python (Part 2) 

Today, I continued to work on web development. I started building app 15 which is a Job Application Form built with django.

Recap on what I did yesterday. I started building a job form application web app with django. I set up a django project and an app in my environment. I also set up the database models and made the database migrations. I created a templates folder to house the html that would be  rendered. Finally, I created a urls.py and edited the views.py in my app directory for the rendering of the html page.

Today, I picked up from where I left of. I wrote the code for the html of the app. I then proceed  to create a form model in a forms.py and this ApplicationForm class is there to help me extract the user data delivered in the POST request and store it in a variable. I used a django form module and the class inherited from this module. After this, I went ahead to store the data in the database. I referred to the Form class in the models.py by calling it in the views.py which contained most of the backend code and used an object.create method to store the data inside the database table. Finally I added the email feature to send the email to the user once the form has been submitted. Django has an email module built with the smtp module and that is what i used to send the email. I was able to test out what I did today and the app flow worked like I wanted from the form submission to the email sending.


Day 53 was good, I am learning more and more each day. I will continue building the app tomorrow.
