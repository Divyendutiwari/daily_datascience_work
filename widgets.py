import pandas as pd 
import streamlit as st
import numpy as np
st.title('Widgets')
name=st.text_input('Enter your name')
if name:
    st.write(f'Hello {name}!')
age=st.slider('Enter your age',0,100,1)
st.write(f'Your age is {age}')
option=st.selectbox('Select your favorite color',['Red','Green','Blue'])
st.write(f'Your favorite color is {option}')
df=pd.DataFrame({'first column':[1,2,3,4],'second column':[10,20,30,40]})
if st.checkbox('Show dataframe'): 
    st.write(df)
st.button('Click me')
df.to_csv('data.csv', index=False)
st.download_button('Download data as CSV',data=df.to_csv(index=False),file_name='data.csv',mime='text/csv')
uploaded_file=st.file_uploader('Upload a file')
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)