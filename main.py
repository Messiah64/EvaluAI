import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json
from pprint import pprint
import pandas as pd
from typing import List, Dict, Tuple
import openai
import numpy as np
import pickle
import tiktoken
import math

from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent

# Initialize session state if not already defined
if 'business_name' not in st.session_state:
    st.session_state.business_name = ""
    st.session_state.business_type = ""
    st.session_state.elevator_pitch = ""

selected = option_menu(
    menu_title=None,
    options=["Home", "Business Layout", "Landing Page Creation"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Display content based on the selected section
if selected == "Home":
    st.title(f"You selected {selected}")
    # Use session_state to store and retrieve variables
    st.session_state.business_name = st.text_input("Business Name", value=st.session_state.business_name)
    st.session_state.business_type = st.text_input("Business Type", value=st.session_state.business_type)
    st.session_state.elevator_pitch = st.text_area("Elevator Pitch", value=st.session_state.elevator_pitch)

    # Create a button to store the variables
    if st.button("Generate Business Layout"):
        pass  
    # OpenAI processing here

if selected == "Business Layout":
    st.title(f"You selected {selected}")
    st.write(f"Displaying stored variables: Business Name: {st.session_state.business_name}, Business Type: {st.session_state.business_type}, Elevator Pitch: {st.session_state.elevator_pitch}")

if selected == "Landing Page Creation":
    st.title(f"You selected {selected}")
