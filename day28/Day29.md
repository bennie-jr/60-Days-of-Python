### DAY 28: App 5 - Email Daily News from API with Python(Part 2)

Today, I finished building app number 5 which accesses news about a particular topic via an API and sends them by email.

Recap on what I did yesterday. I started building app number 5. I signed up for newsapi.org, generated the
api key and the api url I will need for this project. I imported the requests module and used it to get the payload in
json and manipulated to see exactly what data I will pick from the payload. I used a for loop to test what kind of data I
can get from this dictionary object. Today, I added the email sending part of the project. Since I was able to use my
side project to send an email with the article title and description, I just worked with that on this app. I just added to
what I had, the email subject and the url for the articles to the email format. After doing this the email was sent
successfully and the outcome was as expected. I also learned how to use a query parameter in a url and I used this to 
edit the api url to return only articles in the English language. Finally, I learned how to download a file from the
web specifically an image with requests module and using the with open method in write binary mode to save that file
or image from the web with the request.content method.


Also, I finished building [side-project](SP-Daily-Astronomy-Image). This project is a webpage which displays the 
Astronomy image of the day, the description and the title from NASA using their api key and api url. I used streamlit
for the frontend. I was able to render the information on the webpage by using the requests module to get the payload
data from the api url. The data was a dictionary in json format so I was able to manipulate the data to render the 
image, the title and the description on the streamlit webpage with streamlit methods of course.
I used a .env file to hide all the sensitive info.

Lastly I learnt about how pythonanywhere by anaconda. An online platform that lets you host, run, and code Python
in the cloud.


All in all, day 28 was good, I am learning more and more each day. I start building app number 6 tomorrow.