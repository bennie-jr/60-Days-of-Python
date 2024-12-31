### DAY 31: App 6 - Build a Weather Data API with Python(Part 3)

Today, I finished building app number 6 which is a Weather Data API. This app basically will help me learn how to build
my own API.

Recap on what I did yesterday. I started exploring and manipulating the weather data I had to work
with(in csv format) with Jupyter notebook. The api was supposed to return the station, date and temperature when a user queries for a particular date and station number. I had to use the .zfill() method because the station number had a lot zeros infront of it before the actual station number. Then I had to read the data frame with pandas and added a conditionto skip the first 20 rows of each file since they werent needed and I had to use the parse dates condition to tell pandas that the date column was to be treated as an actual date. To get the temperature, I had to use the .loc method to match the exact date that the user was looking for in the exact station file, I addded the .squeeze method to only give me the exact temperature number. I was able to get the API to return exactly what the user was requesting. Today, I had to add the data table to the webpage. The data table contained the station
names and id number. This table helps the user make the exact queries with the exact information the user needs to make the queries.
I also added url endpoints to get all data for a particular station and all data for a specific station at a particular year. I created routes and functions to get the data. I followed the same logicI used for the first url endpoint. I was able to complete
app number 6 and everything was rendered exactly as I wanted.

I also learned about data analysis and visualization theory.

All in all, day 31 was good, I am learning more and more each day. I will start building app number 7 tomorrow.