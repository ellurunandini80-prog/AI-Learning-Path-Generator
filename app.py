import streamlit as st
from utils import generate_learning_path

st.set_page_config(page_title="AI Learning Path Generator")

st.title("📚 AI Learning Path Generator")

goal = st.text_input("Enter your learning goal")

if st.button("Generate Learning Path"):
    if goal:
        with st.spinner("Generating..."):
            result = generate_learning_path(goal)
            st.markdown(result)
    else:
        st.warning("Please enter a learning goal")