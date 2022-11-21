import streamlit as st
import pandas
from send_email import send_email

country = pandas.read_excel("Country.xlsx")
st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message")
    user_country = st.selectbox('Where are you from?', (country))
    raw_message = f"""\
Subject: New Email From {user_email}

From: {user_email}
{user_message}
{user_country}
"""

    submit_button = st.form_submit_button("Submit")

    if submit_button:

        try:
            send_email(raw_message, user_email)
            st.info("Your email was sent successfully!")
        except:
            st.info("Something is wrong. Please kindly check if the email address is correct or try again later.")