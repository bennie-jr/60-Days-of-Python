import streamlit as st
import plotly.express as px
import pandas as pd


dates = []
temperatures = []


with open("data.txt", 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        new = line.split(",")
        dates.append(new[0])
        temperatures.append(new[1])



temperature_figure = px.line(x = dates, y = temperatures, labels={"x": "Date", "y": "Temperature(C)"})
st.plotly_chart(temperature_figure)
