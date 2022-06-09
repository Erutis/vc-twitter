
import streamlit as st
from aitextgen import aitextgen
import time

st.set_page_config(page_title='TLAS')
st.title("TLAS")
st.header("Thought Leadership as a Service")
st.subheader("Don\'t know what to post today? We can help!")
st.image('https://img.huffingtonpost.com/asset/57e3a2a91800002f00316523.jpeg?ops=scalefit_720_noupscale&format=webp')
st.write("This site is helpful for professionals in the venture capital space who are looking to emulate a great VC!\n Click on the button below to generate some content!")


def text_gen():
    ai = aitextgen(model_folder="https://drive.google.com/drive/folders/1-9Oy1ER7zqKSmztCjxi8qko0gcmNlofu?usp=sharing", to_gpu=False) 
    st.session_state['text'] = ai.generate_one(max_length=100, min_length=20)

text1 = st.button(label='Push me for thought leadership', on_click=text_gen)

try:
    st.write(st.session_state['text'])
except:
    st.write('This will change to text once you press the button.')

st.write("[Project Github](https://github.com/Erutis/vc-twitter)")


