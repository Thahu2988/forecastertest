import streamlit as st
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS (FIXED for hiding top-right controls) ---
st.markdown("""
<style>
/* Hide the top Streamlit header (contains the three-dot menu, "Manage app", and "Share") */
/* We target multiple elements to ensure thorough hiding across different Streamlit versions */
header, 
div[data-testid="stDecoration"],
div[data-testid="stAppViewerControlPanel"],
div[data-testid="stToolbar"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important; /* Ensures no empty space is left behind */
    padding: 0 !important;
}

/* Hide bottom-right status widget */
[data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
}

/* Hide footer and main menu */
footer, #MainMenu {display: none !important;}

/* Hide sidebar and its toggle (This is what hides the default "Home" navigation) */
section[data-testid="stSidebar"],
button[title="Toggle sidebar"],
button[title="Open sidebar"],
button[title="Hide sidebar"] {
    display: none !important;
}

/* --- Page Styling --- */
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
# Note: st.columns(2) is simpler than st.columns([0.5, 0.5])
# The inner use_container_width=True ensures the buttons fill the space of their respective columns.
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
