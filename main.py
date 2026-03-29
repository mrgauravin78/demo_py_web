import streamlit as st
import pandas as pd

st.title("Welcome to my website")
st.header("Pyton Tuts")
st.subheader("hello world")
st.markdown("loving this")
st.code("""for i in range(1,5,1):
                print("hello")
""")

dataset = pd.read_csv("tbl_employees.csv")
st.dataframe(dataset)

st.subheader("Form Example")

name = st.text_input("Enter Your Name: ")
fname = st.text_input("Enter Your Father's Name: ")
addr = st.text_area("Enter Your Address: ")
classdata = st.selectbox("Enter Your Class: ", (1,2,3,4,5))
button = st.button("Submit Now")

if(button) :
    st.markdown(f"""
        Name: {name}
        Father's Name: {fname}
        Address: {addr}
        Class: {classdata}
    """)