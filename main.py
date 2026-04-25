import streamlit as st
from Problem_1_TicTacToe.tictactoe_ui import run_tictactoe
from Problem_8_Navigation.navigation_ui import run_navigation

# Page config
st.set_page_config(page_title="AI Problem Solving", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main {background-color: #0e1117;}
    h1 {color: #00ffcc;}
    .stButton>button {
        background-color: #00ffcc;
        color: black;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 AI Problem Solving Dashboard")

option = st.sidebar.radio(
    "Select Problem",
    ["🎮 Tic Tac Toe AI", "🧭 Smart Navigation"]
)

if option == "🎮 Tic Tac Toe AI":
    run_tictactoe()
else:
    run_navigation()