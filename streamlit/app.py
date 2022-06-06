import streamlit as st
#import gpt_2_simple as gpt2
from text_gen import generate_text

st.title("TLAS")
st.header("Thought Leadership as a Service")
st.subheader("Don\'t know what to post today? Why not have an AI help?")


st.button('Generate Thought Leadership', on_click=generate_text)

# function to run the button using the fine-tuned model run2


