
import streamlit as st
import gpt_2_simple as gpt2
import time

st.set_page_config(page_title='TLAS')
st.title("TLAS")
st.header("Thought Leadership as a Service")
st.subheader("Don\'t know what to post today? Why not have an AI help?")
st.image('https://img.huffingtonpost.com/asset/57e3a2a91800002f00316523.jpeg?ops=scalefit_720_noupscale&format=webp')
st.write("This site is helpful for professionals in the venture capital space who are looking to emulate a great VC!\n Click on the button below to generate some content!")

# use @st.cache to speed up text_gen by 50%
# this will mean you can only press the button once

@st.cache()
def text_gen():
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, checkpoint_dir='/Users/kei/Downloads/checkpoint', run_name='run3') 
    st.session_state['text'] = gpt2.generate(sess, checkpoint_dir='/Users/kei/Downloads/checkpoint', return_as_list=True, length=50, run_name='run3')[0]


text1 = st.button(label='Push me for thought leadership', on_click=text_gen)

st.write(st.session_state['text'])

st.write("[Project Github](https://github.com/Erutis/vc-twitter)")


