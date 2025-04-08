import streamlit as st
from main import page_1

st.title("Page Two")

st.write("Welcome to page two. Nothing going on here either. Want to head back to page one?")

# Create a button that navigates to page one when clicked
if st.button("Go to page one"):
    st.switch_page("first_page.py")