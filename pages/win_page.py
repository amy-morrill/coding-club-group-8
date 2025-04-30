import streamlit as st
st.balloons()
st.markdown("<h1 style=’text-align: center; color: blue;’>Fantastic work!</h1>", unsafe_allow_html=True)
st.write("Thanks to your sharp thinking, the lab is safe, and we’re one step closer to advancing scientific discovery. Keep your mind sharp and ready for the next mission—science never stops, and neither do we! See you next time!")
if st.button("Solve for more words!"):
    del st.session_state["selected_word"]
    del st.session_state["good_guesses"]
    del st.session_state["inventory"]
    del st.session_state["bad_guesses"]
    st.switch_page("game_page.py")