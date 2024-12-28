### DAY 30: App 6 - Build a Weather Data API with Python(Part 2)

Today, I continued building app number 6 which is a Weather Data API. This app basically will help me learn how to build
my own API.

Recap on what I did yesterday. I started building the Weather Data API which is app 6. I started building the website with flask. I built the html page the app needed which consisted of just a header element and a paragraph which was like a little documentation for the api. I went ahead to build the api. I added two routes, the first route rendered the html page which displayed the api documentation. The second route rendered a second page which displays the results when a user makes a query(calling the api url). All I did in regard to building the api was to play with how to return a dictionary when the api url is called. I was able tp render what I wanted and the flask app run successfully. Today, I started exploring and manipulating the weather data I had to work
with(in csv format) with Jupyter notebook. I had to go in depth with data analysis with pandas its methods. After I had somewhat of
a firm grasp on the concept of data manipulation with pandas, I went ahead to build the api that will return when the user makes a
query. The api was supposed to return the station, date and temperature when a user queries for a particular date and station 
number. To be able to do this I had to get a filename format that the station number the user queries will fit in to find the 
exact station file since the files for the stations are in a folder. I had to use the .zfill() method because the station number
had a lot zeros infront of it before the actual station number. Then I had to read the data frame with pandas and added a condition
to skip the first 20 rows of each file since they werent needed and I had to use the parse dates condition to tell pandas that the 
date column was to be treated as an actual date. To get the temperature, I had to use the .loc method to match the exact date that 
the user was looking for in the exact station file, I addded the .squeeze method to only give me the exact temperature number. I was able to get the API to return exactly what the user was requesting.

I also took a jupyter labs and using the jupyter notebook since it is very convenient for data analysis.


Also, I continued building [side-project](SP-Translator-API) from yesterday. I had done most of the work yesterday, I just needed
to add the definitions of the word the user was querying to the API data that was being returned. I used pandas to read the csv file
and used the .loc and squeeze pandas methods to get the exact definition of the word the user was querying. I was able to do this
successfully and the application worked like I needed it to. 


All in all, day 30 was good, I am learning more and more each day. I will finish building app number 6 tomorrow.