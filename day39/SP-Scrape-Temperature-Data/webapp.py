import streamlit as st
import plotly.express as px
import pandas as pd
import sqlite3


dates = []
temperatures = []

connection = sqlite3.connect("temp-date.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM temperature")
data = cursor.fetchall()

for d,t in data:
    dates.append(d)
    temperatures.append(t)




temperature_figure = px.line(x = dates, y = temperatures, labels={"x": "Date", "y": "Temperature(C)"})
st.plotly_chart(temperature_figure)
