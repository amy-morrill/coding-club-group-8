import streamlit as st
import random 

st.title("Build a Scientist")

game_words = ['Genetic','Histology','Sequence','Clinical Trial','Mutation','Genome','Oncology']

def game_word_generator(word): 
    st.write(word)
    st.write(f"`{' '.join(['_'] * len(word))}`")
    
if game_words:
    selected_word = random.choice(game_words)

game_word_generator(st.session_state.selected_word)
   
# Session state
if 'selected_word' not in st.session_state:
    st.session_state.selected_word = st.session_state.selected_word

# Create function to evaluate the guess
def eval_guess():
    if st.session_state.guess:
        if st.session_state.guess in st.session_state.selected_word:
            st.success("Good guess!")
            st.write()
        else: 
            st.error("Try again")

guess = st.text_input("Guess a letter:", key="guess", on_change = eval_guess)
 
        
 