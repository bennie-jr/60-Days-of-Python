### DAY 33: App 7 - Build a Weather Forecast Dashboard Python(Part 2)

Today, I completed app number 7 which is a Weather Forecast. This app will forecast the weather for the next 5
days in any city or town on earth using a weather API as the data source.

Recap on what I did yesterday. I was able to finish building the UI and rendered some dummy data for the graph
visualization. Today, I added more functionality to the application. After writing the frontend yesterday, I added
the backend. The backend was a function that requested the API data from the openweathermap api and manipulated and
returned the filtered json API data. I imported the backend to the frontend to make the connection. I added two
if statements to the frontend code that based on the user choices of place and days between 1-5 if the user selects
temperature the data will be displayed as a plotted graph of the tempratures and dates. The second if condition
displayed images of the sky conditions(clear, clouds, rain etc) based on the user selection. I was able to complete the app
and it ran like I expected it to. I also fixed two bugs, one being handling a KeyError when a user inputs a place
that does not exists. I fixed it by introducing a try and except block into the code. The second bug I fixed was
with the y axis of the graph which displayed the temperature in degree celsius which had been multiplied by 10
so the accurate temperature was not showing. I fixed it by simply dividing the filtered data from the api data 
by 10.  


All in all, day 33 was good, I am learning more and more each day. I will start building app number 8 tomorrow.