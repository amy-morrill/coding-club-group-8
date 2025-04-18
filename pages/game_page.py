import streamlit as st
import random

st.title("Build a Scientist")

# Display scientist  
# st.image("images/scientist-beaker-test-tube-animated-f.gif")
# Display scientist with equipment 

game_words = ['Genetic','Histology','Sequence','Clinical Trial','Mutation','Genome','Oncology']

def game_word_generator(word):
    st.write("".join("_" * len(word)))

if game_words:
    selected_word = random.choice(game_words)
    game_word_generator(selected_word)
