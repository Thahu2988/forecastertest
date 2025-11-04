import streamlit as st
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
st.markdown("""
<style>
/* Hide Streamlit Cloud "Manage app" tab (top-right black tab) */
div[data-testid="stAppViewerControlPanel"] {
    display: none !important;
    visibility: hidden !important;
}

/* Hide bottom-right status widget */
[data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
}

/* Hide footer and top-right menu */
footer, #MainMenu {display: none !important;}

/* Hide Streamlit toolbar (Share, etc.) */
[data-testid="stToolbar"] {
    display: none !important;
    visibility: hidden !important;
}

/* Hide the sidebar toggle (top-left arrow) completely */
button[title="Toggle sidebar"],
button[title="Open sidebar"],
button[title="Hide sidebar"],
section[data-testid="stSidebar"] {
    display: none !important;
}

/* --- Centered main layout --- */
.main-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 90vh;
    text-align: center;
    margin-top: -5vh;
}

/* --- Button styling for navigation --- */
.menu-button {
    background-color: #f0f2f6;
    color: #000;
    padding: 0.8em 2.2em;
    margin: 0.5em;
    border-radius: 8px;
    border: none;
    font-size: 1.1em;
    cursor: pointer;
    transition: all 0.2s ease;
}
.menu-button:hover {
    background-color: #004080;
    color: white;
}

/* --- Title and subtitle styling --- */
h1 {
    margin-bottom: 0.2em;
}
.subtext {
    font-size: 1.1em;
    color: #444;
    margin-bottom: 1.5em;
}
</style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.title("🛠️ Maldives Meteorological Service Tools")
st.markdown('<p class="subtext">Select a forecast tool to begin</p>', unsafe_allow_html=True)

# Centered navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌧️ Rainfall Outlook", key="rain"):
        st.switch_page("pages/Rainfall_Outlook.py")
    if st.button("🌡️ Temperature Outlook", key="temp"):
        st.switch_page("pages/Temperature_Outlook.py")

st.markdown('</div>', unsafe_allow_html=True)

# --- App runtime caption ---
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.caption(f"App running as of {st.session_state['start_time']} (Time Zone: Malé, Maldives)")
