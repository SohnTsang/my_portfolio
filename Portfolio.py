import streamlit as st
import pandas


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .css-15zrgzn {display: none}
        .css-eczf16 {display: none}
        .css-jn99sy {display: none}
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)


st.markdown("<h2 style='text-align: center; color: white;'>Sohn's Portfolio</h2>", unsafe_allow_html=True)

content = """
This is my python portfolio created from Udemy bootcamp.
"""
st.markdown(f"<h3 style='text-align: center; color: grey;'>{content}</h3>", unsafe_allow_html=True)

st.text("")
st.text("")
st.markdown("***")
st.text("")
st.text("")

empty_col3, col1, empty_col, col2, empty_col2, col3, empty_col4 = st.columns([0.5, 1, 0.2, 1, 0.2, 1, 0.5])


df = pandas.read_csv("data.csv", sep=";")

with col1:
    for index, row in df[:7].iterrows():
        st.markdown(f"<h4>{str(index + 1) + '. ' + row['title']}</h4>", unsafe_allow_html=True)
        st.text("")
        st.markdown(f"<h6>{row['description']}</h6>", unsafe_allow_html=True)
        st.image("images\\" + row["image"])
        st.write(f"[Source Code] {row['url']}")
        st.text("")

with col2:
    for index, row in df[7:14].iterrows():
        st.markdown(f"<h4>{str(index + 1) + '. ' + row['title']}</h4>", unsafe_allow_html=True)
        st.text("")
        st.markdown(f"<h6>{row['description']}</h6>", unsafe_allow_html=True)
        st.image("images\\" + row["image"])
        st.write(f"[Source Code] {row['url']}")
        st.text("")

with col3:
    for index, row in df[14:].iterrows():
        st.markdown(f"<h4>{str(index + 1) + '. ' + row['title']}</h4>", unsafe_allow_html=True)
        st.text("")
        st.markdown(f"<h6>{row['description']}</h6>", unsafe_allow_html=True)
        st.image("images\\" + row["image"])
        st.write(f"[Source Code] {row['url']}")
        st.text("")



