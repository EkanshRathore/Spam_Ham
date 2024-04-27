import streamlit as st
import joblib

model = joblib.load('spam-ham')
st.title('SPAM-HAM CLASSIFIER')  # IT gives title
ip = st.text_input("Enter The Message")  #IT Creates A Textbox
op = model.predict([ip])
if st.button("Predict"):  # Creates A button with name predict
    st.title(op[0])  #The 0th Element in the op variable is displayed as a title
