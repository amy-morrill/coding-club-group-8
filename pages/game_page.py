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

# Display and update the game word as player enters new guesses 
def game_word_generator(word):
    st.write(word)
    # Create a display string with underscores for each letter in the word
    if not st.session_state.good_guesses:
        final_word = st.write(f"`{' '.join(['_'] * len(word))}`")
    else:
        final_word = ' '.join([guess if guess in st.session_state.good_guesses else '_' for guess in word])
    st.write(final_word)
    
# st.write(st.session_state.good_guesses)
# st.write(st.session_state.bad_guesses)

game_word_generator(st.session_state.selected_word)

# Create function to evaluate the guess
def eval_guess():
    guess = st.session_state.guess
    if guess:
        if guess in st.session_state.selected_word.lower():
            st.session_state.good_guesses.append(guess) 
            st.success("Good guess!")
        else: 
            st.session_state.bad_guesses.append(guess)
            st.error("Try again") 

guess = st.text_input("Guess a letter:", key="guess", on_change=eval_guess)