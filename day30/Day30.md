### DAY 29: App 6 - Build a Weather Data API with Python(Part 1)

Today, I started building app number 6 which is a Weather Data API. This app basically will help me learn how to build
my own API.

Recap on what I did yesterday. I added the email sending part of the project. I just added to
what I had, the email subject and the url for the articles to the email format. After doing this the email was sent
successfully and the outcome was as expected. I was able to finish building app5. Today, I started building the Weather
Data API which is app 6. I started with a short crash course on writing HTML because I need html for this app for
the front end. Now to the app itself, I started building the website with flask. I need to import the flask module
to be able to use it. I built the html page the app needed which consisted of just a header element and a paragraph
which was like a little documentation for the api. I went ahead to build the api. This was like a "learn as you go" kind
of building cos I was learning flask as I was writing the code. I added two routes, the first route rendered the html
page which displayed the api documentation. The second route rendered a second page which displays the results when a 
user makes a query(calling the api url). I had to write function definition for both routes because that is how flask 
works and I had to dump the html file into a templates folder also because that is how flask reads static webpages. All 
I did today in regard to building the api was to play with how to return a dictionary when the api url is called. I 
was able tp render what I wanted and the flask app run successfully. I will go into the main functionality of this app
tomorrow.


Also, I started building [side-project](SP-Translator-API). This project is a webpage which displays the meaning of a 
word when a user queries the api with any word. It is basically a dictionary. I started with the frontend a basic
html page which displays the documentation of the API. It has a title and two paragraphs which gives you a URL format
and an example URL format. I added the api which of which I am using flask so I basically followed the format I used 
for app6. I imported flask and write two routes with each route having its own function. I haven't added the data source
yet so the second route was just a test to display a dictionary of the definition and the word that the user is querying.
The definition I used as a test function was just the word being queried but capitalized. The first route rendered the
html page. What I wanted to achieve was rendered successfully and I will finish building this tomorrow. 



All in all, day 29 was good, I am learning more and more each day. I continue building app number 6 tomorrow.