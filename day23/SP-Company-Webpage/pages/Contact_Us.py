import pandas
import streamlit as st
from send_emails import send_email

df = pandas.read_csv("topics.csv")

with st.form(key="my_form"):
    user_email = st.text_input("Your Email Address")
    topic_option = st.selectbox(
        "Which topic would you like to discuss?",
        df,
        index=None,
        placeholder="Select topic...",
    )
    raw_message = st.text_area("Your message")
    message = f"""\
    Subject: New email from {user_email}
    
    From: {user_email}
    Topic {topic_option}
    {raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email sent successfully")
