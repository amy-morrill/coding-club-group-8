import streamlit as st
from streamlit_extras.let_it_rain import rain
rain(emoji="😢",font_size=54, falling_speed=5)
st.markdown("<h1 style=’text-align: center; color: red;’>Oh No!!!</h1>", unsafe_allow_html=True)
st.write("I’m Sorry! We have no more inventory to complete this mission. Please try again to save the scientist!")
if st.button("Solve for more words!"):
    del st.session_state["selected_word"]
    del st.session_state["good_guesses"]
    del st.session_state["inventory"]
    del st.session_state["bad_guesses"]
    st.switch_page("game_page.py")