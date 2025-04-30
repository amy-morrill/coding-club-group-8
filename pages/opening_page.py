import streamlit as st

# Create title for page
st.markdown("<h1 style='text-align: center; color: gray;'>Build A Scientist</h1>", unsafe_allow_html=True)

# This is a function that sets the user name variable to the value of
# user_name_text_input and sets user_name_text_input back to the empty string
def submit_user_name():
    if st.session_state.user_name_text_input:
        st.session_state.user_name = st.session_state.user_name_text_input
    st.session_state.user_name_text_input = ""

# This is a variable called user_name that is initialized to be the empty string ""
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if not st.session_state.user_name:
    # This is an input text box
    # Adding key = "user_name_text_input" automatically saves the value of the text input to a variable in
    # session_state called user_name_text_input (referenced in submit_user_name function)
    st.text_input("What's your name?", key="user_name_text_input", on_change=submit_user_name)
 
# If a user name is saved, write a message using it and display an image
if st.session_state.user_name:
    st.write(f"Hello, {st.session_state.user_name}! I’m Dr. Doofenshmirtz and I need your help! The future of science depends on you guessing a mystery word. But be careful—every wrong guess makes me lose a piece of equipment one by one! We need your skills to guess the right letters. You’ll have [7] guesses each time. Let’s get started!")
    
    # Display the scientist
    st.image("images/scientist-beaker-test-tube-animated-f.gif")
    
    # Add a "Start Game" button
    if st.button("Start Game"):
        st.switch_page("game_page.py")