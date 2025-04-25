import streamlit as st

page_1 = st.Page("opening_page.py", title="Opening page")
page_2 = st.Page("game_page.py", title="Game page")
page_3 = st.Page("end_page.py", title="End page")
pages = st.navigation([page_1, page_2], position="hidden")
pages.run()