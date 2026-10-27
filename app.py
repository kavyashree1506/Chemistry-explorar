
import streamlit as st

st.set_page_config(
    page_title="Chemistry Explorer",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Chemistry Explorer")
st.write("Welcome to your interactive Chemistry learning app!")

topic = st.selectbox(
    "Choose a chemistry topic",
    ["Atomic Structure", "Chemical Bonding", "Periodic Table"]
)

if topic == "Atomic Structure":
    st.header("Atomic Structure")
    st.write("Atoms contain protons, neutrons, and electrons.")
    st.write("Atomic number = Number of protons.")

elif topic == "Chemical Bonding":
    st.header("Chemical Bonding")
    st.write("Ionic bonds involve electron transfer.")
    st.write("Covalent bonds involve sharing electrons.")

elif topic == "Periodic Table":
    st.header("Periodic Table")
    st.write("The periodic table organizes elements by atomic number.")

st.success("Explore chemistry one topic at a time!")
