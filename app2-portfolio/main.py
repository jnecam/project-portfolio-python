import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.jpg", width=400)

with col2:
    st.info("Hi, I am a Joseph Emeka! I am a Python Programmer. I had my master's in 2022 in Computer Science at the "
            "University of Central Oklahoma."
            "I am currently working as DevOps Engineer. My expertise includes technologies such as Docker, Kubernetes, "
            "Ansible, and Jenkins, as well as experience with cloud platforms like AWS")
