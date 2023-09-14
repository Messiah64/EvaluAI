import streamlit as st
from streamlit_option_menu import option_menu

# as side bar
selected = option_menu(
        menu_title = None, # compulsory
        options = ["Home", "Projects", "Contact"], 
        icons = ["house", "book", "envelope"], # optional
        menu_icon = "cast",
        default_index = 0,    
        orientation = "horizontal")


def upload():
    None

    

if selected == "Home":
    with st.form(key = "form"):
        st.title(f"Welcome to my {selected} page")
        input_name = st.text_input("Business Name", key = 1)
        input_desc = st.text_input("Elevator Pitch", key = 2)

        if st.form_submit_button("Submit"):
            upload()

if selected == "Projects":
    st.title(f"Welcome to my {selected} page")
if selected == "Contact":
    st.title(f"Welcome to my {selected} page")
