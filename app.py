import streamlit as st

st.set_page_config(page_title="Docuwise", page_icon="📄")

st.title("Docuwise - My First App")
st.write("App is live")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome {name}!")
