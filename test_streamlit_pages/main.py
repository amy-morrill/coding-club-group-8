import streamlit as st

page_1 = st.Page("first_page.py", title="First page")
page_2 = st.Page("second_page.py", title="Second page")
pages = st.navigation([page_1, page_2], position="hidden")
pages.run()