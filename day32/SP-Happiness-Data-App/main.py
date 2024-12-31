import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")


x_option = st.selectbox("Select data for the X-axis", 
                       ("GDP", "Happiness", "Generosity"))

y_option = st.selectbox("Select data for the Y-axis", 
                       ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")

match x_option:
    case "GDP":
        x_array = df['gdp']
    case "Happiness":
        x_array = df['happiness']
    case "Generosity":
        x_array = df['generosity']


match y_option:
    case "GDP":
        y_array = df['gdp']
    case "Happiness":
        y_array = df['happiness']
    case "Generosity":
        y_array = df['generosity']



st.subheader(f"{x_option} and {y_option}")

figure = px.scatter(x=x_array, y=y_array, labels={"x": f"{x_option}", "y": f"{y_option}"})
st.plotly_chart(figure)
