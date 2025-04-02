import streamlit as st

# Create Page Title
st.title("Amy's Sample UI")
if "user_name_str" not in st.session_state:
    st.session_state.user_name_str = ""
# Create function to save user name when inputted
def submit_user_name():
    if st.session_state.user_name_input:
        st.session_state.user_name_str = f"Hi, {st.session_state.user_name_input}! Welcome to my UI"
    st.session_state.user_name_input = ""
# Create test input for user name
name = st.text_input("What's your name?", key="user_name_input", on_change=submit_user_name)
# Save user name in session state so it persists
st.write(st.session_state.user_name_str)

# Save reveal scientist button click status
if 'reveal_scientist_clicked' not in st.session_state:
    st.session_state.reveal_scientist_clicked = False

def click_reveal_scientist_button():
    st.session_state.reveal_scientist_clicked = True

st.button('Reveal scientist!', on_click=click_reveal_scientist_button)

if st.session_state.reveal_scientist_clicked:
    st.image("images/scientist-beaker-test-tube-animated-f.gif")

if st.button("Send balloons!"):
    st.balloons()
