import streamlit as st
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS (The definitive fix for hiding all Streamlit chrome) ---
st.markdown("""
<style>
/* 1. HIDE ALL TOP STREAMLIT CONTROLS (Header, Share, Settings, 3-dots/Manage App) */

/* The main header bar (contains the icons) */
header, 
div[data-testid="stDecoration"],
div[data-testid="stToolbar"], 
div[data-testid="stAppViewerControlPanel"], 
button[data-testid="stActionButton"],
/* Highly specific class for the floating menu container */
.st-emotion-cache-12fmufv,
/* Targets the entire app header that wraps the controls */
div[data-testid="stAppViewContainer"] > header { 
    display: none !important;
    visibility: hidden !important;
    height: 0 !important; 
    min-height: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    opacity: 0 !important;
    pointer-events: none !important; /* Prevents accidental clicks */
}

/* 2. HIDE BOTTOM "MANAGE APP" BAR */

/* Targets the bottom-right status widget */
[data-testid="stStatusWidget"],
/* Targets the persistent footer bar that holds the "Manage App" link */
div[data-testid="stBottomBlock"],
/* Targets the official Streamlit footer if it is rendered */
footer {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important; 
    min-height: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    opacity: 0 !important;
    pointer-events: none !important;
}

/* Hide old/other Streamlit default elements */
#MainMenu {display: none !important;}

/* 3. HIDE SIDEBAR AND ITS TOGGLE */
/* This is why you cannot see the default "Home" button */
section[data-testid="stSidebar"],
button[title="Toggle sidebar"],
button[title="Open sidebar"],
button[title="Hide sidebar"] {
    display: none !important;
}

/* --- Page Styling (Kept untouched) --- */
body {
    background-color: #f8f9fa;
}

.header-container {
    text-align: center;
    padding-top: 2.5rem;
    padding-bottom: 1rem;
}

/* Button row centered tightly together */
.button-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;  /* Controls the space between buttons */
    margin-top: 1rem;
    margin-bottom: 1.2rem;
}

/* Buttons styling */
.menu-button {
    background-color: #f0f2f6;
    color: #000;
    padding: 0.8em 2em;
    border-radius: 8px;
    border: none;
    font-size: 1.05em;
    cursor: pointer;
    transition: all 0.2s ease;
}
.menu-button:hover {
    background-color: #004080;
    color: white;
}

/* Subtext and caption */
.subtext {
    font-size: 1.1em;
    color: #444;
    margin-top: 0.5em;
}
.caption {
    font-size: 0.9em;
    color: #777;
    margin-top: 0.3em;
}
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.title("🛠️ Maldives Meteorological Service Tools")

# --- Two Buttons Close Together Below Title ---
st.markdown('<div class="button-row">', unsafe_allow_html=True)

# Using columns for the buttons
col1, col2 = st.columns(2) 
with col1:
    # This button switches to the Rainfall Outlook page
    if st.button("🌧️ Rainfall Outlook", key="rain", use_container_width=True):
        st.switch_page("pages/Rainfall_Outlook.py")
with col2:
    # This button switches to the Temperature Outlook page
    if st.button("🌡️ Temperature Outlook", key="temp", use_container_width=True):
        st.switch_page("pages/Temperature_Outlook.py")
st.markdown('</div>', unsafe_allow_html=True)

# --- Subtext and Timestamp ---
st.markdown('<p class="subtext">Select a forecast tool to begin</p>', unsafe_allow_html=True)

if 'start_time' not in st.session_state:
    st.session_state['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.markdown(
    f'<p class="caption">App running as of {st.session_state["start_time"]} (Time Zone: Malé, Maldives)</p>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
