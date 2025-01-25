import streamlit as st
import plotly.express as px
import pandas as pd
from pathlib import Path
import glob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer



filepaths = glob.glob("diary/*.txt")
filepaths.sort()

get_date = []
positivity_scores = []
negativity_scores = []

for file in filepaths:
    with open(file, 'r') as f:
        content = f.read()
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(content)
        positivity_scores.append(score['pos'])
        negativity_scores.append(score['neg']) 
    filename = Path(file).stem
    get_date.append(filename)
   

dates = sorted(get_date)


st.title("Diary Tone")


st.subheader("Positivity")

positivity_figure = px.line(x = dates, y = positivity_scores, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(positivity_figure)


st.subheader("Negativity")

negativity_figure = px.line(x = dates, y = negativity_scores, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(negativity_figure)