import streamlit as st
st.title("welcome to streamlit")
st.text("aaj hum sikh rahe hai Git")
st.write("pehla commit to ho gya ab dusra commit karte hai bhaisahab")

st.header("ye hai pehla header")
st.header('ye wala 2nd header hai')

st.sidebar.title("courses")
st.sidebar.markdown("""
-Home
-About
-Contact
""")
