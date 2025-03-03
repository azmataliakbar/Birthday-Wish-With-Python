import streamlit as st
import time
from PIL import Image
import random

# Page configuration
st.set_page_config(page_title="Birthday Card", page_icon="🎉", layout="centered")

st.markdown("""
    <style>
    /* Global styles */
    body {
        background-color: black !important;
        color: white !important;
    }

    .stApp {
        background-color: black !important;
    }

    /* Title and Header styles */
    h1, h2, h3, h4, h5, h6, .stMarkdown h1 {
        color: white !important;
    }

    /* Custom style for animated title to override red color */
    h1.animated-title {
        color: #05fc2a !important;  /* Green color with !important to override global red */
        text-align: center !important;  /* Center align the title */
    }

    /* Sidebar styles for dark gray background */
    .stSidebar, .stSidebar [data-testid="stSidebar"], .stSidebar .css-ng1t4o, .stSidebar .css-1d391kg {
        background-color: #2f2f2f !important;
        color: white !important;
    }

    /* Custom button styles */
    .stButton button {
        background-color: #363940 !important;
        color: orange !important;
        border: 2px solid lightgray !important;
        border-radius: 8px !important;
        padding: 15px 0px !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        margin: 5px !important;
        width: 100% !important;
        transition: background-color 0.3s !important;
    }

    .stButton button:hover {
        background-color: #4A4D55 !important;
    }

    /* Progress bar styles */
    .stProgress > div > div {
        background-color: #02fa51 !important;
    }

    /* Center align all text by default, except animated title */
    .stMarkdown, h1,h3, h5, h6 {
        text-align: center !important;
        color: red !important;
    }
    stMarkdown, h2 {
        text-align: center !important;
        color: #054bfc !important;
    }
    .stMarkdown, h4 {
        text-align: center !important;
        color: #05fc2a !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🐍 Python : Birthday Greeting 🍰")

# Custom function to display animated title
def animated_title(title):
    animated_text = ""
    for char in title:
        animated_text += char
        st.markdown(f"<h1 class='animated-title'>{animated_text}</h1>", unsafe_allow_html=True)
        time.sleep(0.1)
        st.empty()  # Clear previous line to create animation effect

# Function to display confetti
def show_confetti():
    for _ in range(3):
        st.balloons()

# Animated Title and Subtitle
animated_title("🎉 Happy 25th Birthday! 🎉")
st.markdown("<h2 style='color: #02fa51;'>🍰 James Anthony 🍰</h2>", unsafe_allow_html=True)
st.markdown("<h4> 📜 March 5th 📜</h4>", unsafe_allow_html=True)

# Display candles
st.markdown("### 🕯️ Light the candles 🕯️:")
candles_lit = st.slider("Candles Lit", min_value=0, max_value=5, step=1)
st.progress(candles_lit / 5)

# Display balloons
st.markdown("### 🎈 Pop the balloons 🎈:")
balloons_popped = st.slider("Balloons Popped", min_value=0, max_value=5, step=1)
st.progress(balloons_popped / 5)

# Celebration button
if st.button("🎁 🎁 🎁 Celebrate! 🎁 🎁 🎁"):
    if candles_lit == 5 and balloons_popped == 5:
        st.success("🎉 All candles lit and balloons popped! Let's celebrate! 🎉")
        show_confetti()
    else:
        st.warning("Please light all candles and pop all balloons first!")

# Author
st.markdown("<h4 style='color: #FFA07A;'>Author: Azmat Ali</h4>", unsafe_allow_html=True)
