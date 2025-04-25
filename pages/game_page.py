import streamlit as st
import random 

st.title("Build a Scientist")

game_words = ['Genetic','Histology','Sequence','Mutation','Genome','Oncology']


if game_words:
    selected_word = random.choice(game_words)

# Session state
if 'selected_word' not in st.session_state:
    st.session_state.selected_word = selected_word
    
if 'good_guesses' not in st.session_state:
    st.session_state.good_guesses = []

if 'bad_guesses' not in st.session_state:
    st.session_state.bad_guesses = []

if 'inventory' not in st.session_state:
    st.session_state['inventory'] =  ["petridish", "microscope", "pipette", "x-ray", "computer", "treatments", "medical gloves"]

# Display and update the game word as player enters new guesses 
def game_word_generator(word):
    st.write(word)
    # Create a display string with underscores for each letter in the word
    final_word = f"`{' '.join([guess if guess.lower() in st.session_state.good_guesses else '_' for guess in word])}`"
    st.write(final_word)

# Create function to evaluate the guess
def eval_guess():
    guess = st.session_state.guess
    if len(guess) == 1:
        if guess in st.session_state.selected_word:
            st.session_state.good_guesses.append(guess) 
            st.success("Good guess!")
        else: 
            st.session_state.bad_guesses.append(guess)
            st.session_state.inventory.pop()
            st.error("Try again") 
    else :
        st.error("Guess must be one character long.")

# Create two columns to put buttons into
scientist_column, inventory_column_1, inventory_column_2 = st.columns([0.5, 0.25, 0.25])

with scientist_column:
    st.image("images/scientist-beaker-test-tube-animated-f.gif", width=700)
    game_word_generator(st.session_state.selected_word)
    guess = st.text_input("Guess a letter:", key="guess", on_change=eval_guess)


with inventory_column_1:
    st.write("Inventory", )
    if "petridish" in st.session_state["inventory"]:
        st.image("images/petridish test.jpg", width=175)
    if "microscope" in st.session_state["inventory"]:
        st.image("images/Microscope.jpg", width=175)
    if "computer" in st.session_state["inventory"]:
        st.image("images/Computer_graphic.jpg", width=175)
    if "medical gloves" in st.session_state["inventory"]:
        st.image("images/medical gloves.jpg", width=200)
with inventory_column_2:
    st.write("")
    if "x-ray" in st.session_state["inventory"]:
        st.image("images/x-ray.jpg", width=250)
    if "treatments" in st.session_state["inventory"]:
        st.image("images/treatments.jpg", width=175)
    if "pipette" in st.session_state["inventory"]:
        st.image("images/Pipette.jpg", width=175)
