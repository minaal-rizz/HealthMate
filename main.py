#to run:  streamlit run main.py 

import streamlit as st

st.title("Hello, Streamlit!")
st.write("I am mahan insan")
st.write("This is a simple Streamlit app.")
st.write("You can use this app to take a picture using your camera.")
st.markdown("# How you doin")
st.markdown("## How you doin")
st.markdown("### How you doin")
st.markdown("#### How you doin")

st.camera_input("Take a picture")

st.success(" This is a success message.")
st.error("This is an error message.")
st.warning("This is a warning message.")
st.info("This is an info message.")
st.exception("This is an exception message.")
#st.help(st.camera_input)

