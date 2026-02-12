



import streamlit as st
import random
from datetime import date




# Page Config
st.set_page_config(page_title="Our Future Dates ❤️", page_icon="🌷")

# Custom Styling
st.markdown("""
    <style>
    /* The whole background */
    .stApp { 
        background-color: #fff5f5; 
    }
    /* Main Title Color */
    h1 { 
        color: #9d174d !important; 
    }
    /* The Date Card */
    .date-card {
        padding: 30px;
        border-radius: 15px;
        background-color: #ffffff;
        border: 3px solid #ffccd5;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    /* Card Text Color - specifically set to dark grey/black for contrast */
    .date-card h2 {
        color: #d63384 !important;
        margin-bottom: 10px;
    }
    .date-card p {
        color: #333333 !important;
        font-size: 1.4rem !important;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)



st.title("The 2026 Date Generator")
st.write("Click the button to reveal our next adventure...")


# 1. The Data: two lists of specific dates and activities
other_dates = [
    "February 28th", 
    "March 14th", "March 27th", 
    "April 11th", "April 25th", 
    "May 9th", "May 23rd"
]

activities = [
    "A cozy movie marathon with way too many snacks 🍿",
    "Spring walk & a picnic 🧺",
    "Late-night gelato 🍦",
    "Visiting a local museum or art gallery 🎨",
    "Sunset hike and a chilled bottle of wine 🍷",
    "Bowling or Mini-Golf (Loser buys pizza!) 🎳",
    "Planning our first summer trip over brunch 🥞"
]

# Logic: February 14th is the "Starting State"
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('🌷 Generate a New Date 🌷', on_click=click_button)

# Logic: pick one from each list
if not st.session_state.clicked:
    # this shows first (feb 14)
    display_date = "February 14th"
    display_activity = "Our first Valentine's <3. A romantic dinner Italian style 🍝"


else:
    # this shows after clicking (random)
    display_date = random.choice(other_dates)
    display_activity = random.choice(activities)
    st.snow()
   



# Display the result
st.markdown(f"""
    <div class="date-card">
        <h2>{display_date}</h2>
        <p>{display_activity}</p>
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("---")
st.caption("Designed with love to my baby")


