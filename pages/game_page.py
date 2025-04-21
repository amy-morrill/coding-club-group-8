import streamlit as st
import random

st.title("Build a Scientist")

game_words = ['Genetic','Histology','Sequence','Clinical Trial','Mutation','Genome','Oncology']

def game_word_generator(word): 
    st.write(word)
    st.write(f"`{' '.join(['_'] * len(word))}`")
    
if game_words:
    selected_word = random.choice(game_words)
    game_word_generator(selected_word)
   
# Session state
if 'selected_word' not in st.session_state:
    st.session_state.selected_word = game_word_generator(selected_word)

# Create a text box for the player to enter a letter
guess = st.text_input("Guess a letter:")

# After players enter a letter, show whether they got it right or wrong
if guess:
    if len(guess) == 1:
        guess    
        if guess in st.session_state.selected_word:
            st.success(f"Good guess!")
        else:
            st.error(f"Sorry - your scientist just lost his [insert equipment name]!")
    else:
        st.error("Please enter 1 letter.")
 