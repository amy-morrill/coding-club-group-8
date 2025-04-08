import streamlit as st

# Create title for page
st.title("Amy's Sample UI")

# Write header
st.header("This is a header", divider="blue")

# This is some text
st.write("This is some text")

# session_state is where data for
# the app is stored
# Here we set a variable called button_click_count to be
# the number 0 if it does not already exist
if "button_click_count" not in st.session_state:
    st.session_state.button_click_count = 0

# This is a function that increments the button click count by one
def increment_button_click_count():
    st.session_state.button_click_count = st.session_state.button_click_count + 1

# This is a function that resets the button click count to zero
def reset_button_click_count():
    st.session_state.button_click_count = 0

# Create two columns to put buttons into
button_column_one, button_column_two = st.columns(2)

# Create a button in column one that calls the increment_button_click_count function
with button_column_one:
    st.button(label="Increment click counter", on_click = increment_button_click_count)

# Create a button in column two that calls the reset_button_click_counter function
with button_column_two:
    st.button(label="Reset button click", on_click = reset_button_click_count)

# This is some text that displays the variable button_click_count variable
st.write(f"Number of button clicks: {st.session_state.button_click_count}")

# This is a variable called user_name that is initialized to be the empty string ""
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# This is a function that sets the user name variable to the value of
# user_name_text_input and sets user_name_text_input back to the empty string
def submit_user_name():
    if st.session_state.user_name_text_input:
        st.session_state.user_name = st.session_state.user_name_text_input
    st.session_state.user_name_text_input = ""

# This is an input text box
# Adding key = "user_name_text_input" automatically saves the value of the text input to a variable in
# session_state called user_name_text_input (referenced in submit_user_name function)
st.text_input("What's your name?", key="user_name_text_input", on_change=submit_user_name)

# If a user name is saved, write a message using it
if st.session_state.user_name:
    st.write(f"Hello, {st.session_state.user_name}! Welcome to this UI!")

# Save a show_cat variable in session_state as False if it doesn't exist
if 'show_cat' not in st.session_state:
    st.session_state.show_cat = False

# Create a function to set the show_cat variable to True
def reveal_cat():
    st.session_state.show_cat = True

# Create a function to set the show_cat variable to False
def hide_cat():
    st.session_state.show_cat = False

st.button('Reveal cat!', on_click=reveal_cat)
if st.session_state.show_cat:
    st.image("https://static.streamlit.io/examples/cat.jpg")
st.button('Hide cat!', on_click=hide_cat)

if st.button("Send balloons!"):
    st.balloons()