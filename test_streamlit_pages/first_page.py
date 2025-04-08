import streamlit as st

# Create title for page
st.title("Page One")

st.write("Welcome to page one. Nothing happening here. Want to try out page two instead?")

# Create a button that navigates to page two when clicked
if st.button("Go to page two"):
    st.switch_page("second_page.py")