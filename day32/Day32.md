### DAY 32: App 7 - Build a Weather Forecast Dashboard Python(Part 1)

Today, I started building app number 7 which is a Weather Forecast. This app will forecast the weather for the next 5
days in any city or town on earth using a weather API as the data source.

Recap on what I did yesterday. I had to add the data table to the webpage. The data table contained the station
names and id number. This table helps the user make the exact queries with the exact information the user needs to make the queries.
I also added url endpoints to get all data for a particular station and all data for a specific station at a particular year. I created routes and functions to get the data. I followed the same logic I used for the first url endpoint. I was able to complete
app number 6. Today, I started buildind app number 7 i.e. Weather Forecast Dashboard. I am using streamlit to help me build the User
Interface. Now to the code, I imported streamlit and plotly. Plotly renders the user data in a visual form like graphs etc. With Ui
of the app, the user has to enter the city they want the forecasted weather for and there is also a slider for days where the user
can pick between 1 to 5 days. There is also an options box where the user selects between Sky and Temperature. The temperature option shows the user the data visualization of the forecasted weather and the Sky option shows a cloud animation of the weather 
every 3 hours till the forecasted time ends. I was able to finish building the UI and rendered some dummy data for the graph
visualization. That is all I did today, I will continue to add more functionality and complete the app tomorrow.

Also, I started building [side-project](./SP-Happiness-Data-App/). This is an app that uses a csv data set and renders a graph visual of the data the user chooses for the x and y axis. Now to the code, I used streamlit to build the UI and plotly to 
render the visual graph and pandas to read the csv dataframe. The user has 3 options(GDP,Happiness and Generosity) in the UI for both the x and y axis and based on the choices the user picks a graph visual of the data will be displayed. I had to use a match
case block since there 3 options each for the x and y axis and this match case block will get the dataframe data that pandas reads.
I was able to get the data and render a scatter plot visual for it. The app worked like I wanted it to.

All in all, day 32 was good, I am learning more and more each day. I will continue building app number 7 tomorrow.