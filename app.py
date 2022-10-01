import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
st.session_state['answer'] = ''!
st.write(st.session_state)
realans = ['', 'abc', 'edf']
if  st.session_state['answer'] in realans:
    answerStat = "correct"
elif st.session_state['answer'] not in realans:
    answerStat = "incorrect"
st.write(st.session_state)
st.write(answerStat)
st.set_page_config(page_title="CAY NHA LA VUON")
data_file=st.file_uploader("Input your file here ",type="xlsx")
if data_file is not None :
    df=pd.read_excel(data_file)
    st.dataframe(df)
    feature=st.text_input("Input label")
    if feature!="" and feature not in df.columns :
        st.warning('Not find feature in data frames', icon="⚠️")
    elif feature in df.columns :
        st.write("Find feature in data frames")
    else:
        st.warning("Not received input")
    
    
    

