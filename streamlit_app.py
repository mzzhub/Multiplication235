import streamlit as st

st.title('Problem - Multiplication235')

st.image("problem.png")

col1, col2, col3 = st.columns([1,1,1])
with col2:
    generate_button = st.button("**Geneate solutions**")

if generate_button:
    st.write("Ai")


