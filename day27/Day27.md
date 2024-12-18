### DAY 27: App 5 - Email Daily News from API with Python(Part 1)

Today, I started building app number 5 which accesses news about a particular topic via an API and sends them by email.

Recap on what I did yesterday. I was able to complete app number 4. Today I started building app number 5. I started by
understanding what API is since I will be using it in this project. I also signed up for newsapi.org, generated the
api key and the api url I will need for this project. I imported the requests module and used it to get the payload in
json and manipulated to see exactly what data I will pick from the payload. The type of the data I got from the request
to the api url was a string so I had to change it to json to fit my need. I used a for loop to test what kind of data I
can get from this dictionary object. That is all I did today, I will add the email sending feature tomorrow with right
data that needs to be added to the email.


Also, I finished building [side-project](SP-Email-API-Data). I just used this project to experiment with the kind of 
data I can send with emails for app 5. I only wanted to send the article title and description from the payload I got from
the api url. I added the send mail python code and imported it into the main python code. I used a for loop to iterate
through the data to get the title and description of the all the articles in the payload. The data I was sending via email
was throwing an error and after researching I had to encode the data in utf-8 format before I could send the email. I was
able to complete this mini project and the email was sent successfully. I used a .env file to hide all the sensitive info.

Lastly I learnt more about how Application Programming Interface(APIs) works.


All in all, day 27 was good, I am learning more and more each day. I finish building app number 5 tomorrow.