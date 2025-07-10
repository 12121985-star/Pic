import streamlit as st
st.title("My Fisrt streamlit App")
st.write("Hello! Creating a simple wen applications using Streamlit.")
name=st.text_input("Enter you name:")
if st.button("submit"):
   st.write (f="Hello,{name}! Welocme to Streamlit.")
