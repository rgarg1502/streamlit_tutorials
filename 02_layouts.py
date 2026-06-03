import streamlit as st

def clean_text(text):
    text = text.replace("~", "").replace("-\n","").replace("\n", " ").strip()
    return text

st.title("lesson 01.02: Intro to Layouts and images")

st.sidebar.image("pydh.jpg", width=100)
st.sidebar.header("Options")
text = st.sidebar.text_area("paste text here") 
button1 = st.sidebar.button("clean Text")

if button1:
    col1, col2 = st.columns(2)
    col1_expander = col1.expander("expand original Text")
    with col1_expander:
        # col1_expander.header("Original Text")
        col1_expander.write(text)

    col2_expander = col2.expander("expand cleaned text")
    clean = clean_text(text)
    with col2_expander:
        # col2_expander.header("Cleaned Text")
        col2_expander.write(clean)

