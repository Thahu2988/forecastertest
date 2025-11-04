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
/* Hide "Manage app" tab (top-right black tab) */
div[data-testid="stAppViewerControlPanel"] {
    display: none !important;
    visibility: hidden !important;
}

/* Hide bottom-right status widget */
[data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
}

/* Hide footer and main menu */
footer, #MainMenu {display: none !important;}

/* Hide Streamlit toolbar (Share, etc.) */
[data-testid="stToolbar"] {
    display: none !important;
    visibility: hidden !important;
}

/* Hide sidebar and its toggle arrow */
button[title="Toggle sidebar"],
button[title="Open sidebar"],
button[title="Hide sidebar"],
section[data-testid="stSidebar"] {
    display: none !important;
}

/* --- Layout Styling --- */
body {
    background-color: #f8f9fa;
}

/* Header container */
.header-container {
    text-align: center;
    padding-top: 3rem;
    padding-bottom: 1rem;
}

/* Centered main content for buttons */
.center-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    height: 70vh;
    text-align: center;
    margin-top: 2rem;
}

/* Buttons */
.menu-button {
    background-color: #f0f2f6;
    color: #000;
    padding: 0.8em 2.2em;
    margin: 0.6em;
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

/* Subtext and caption */
.subtext {
    font-size: 1.1em;
    color: #444;
    margin-bottom: 0.3em;
}
.caption {
    font-size: 0.9em;
    color: #777;
    margin-top: 0.3em;
}
</style>
""", unsafe_allow_html=True)

# --- Header (Top of Page) ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.title("🛠️ Maldives Meteorological Service Tools")
st.markdown('<p class="subtext">Select a forecast tool to begin</p>', unsafe_allow_html=True)

# --- Initialize and Display App Run Time ---
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f'<p class="caption">App running as of {st.session_state["start_time"]} (Time Zone: Malé, Maldives)</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Centered Buttons Below ---
st.markdown('<div class="center-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌧️ Rainfall Outlook", key="rain"):
        st.switch_page("pages/Rainfall_Outlook.py")
    if st.button("🌡️ Temperature Outlook", key="temp"):
        st.switch_page("pages/Temperature_Outlook.py")
st.markdown('</div>', unsafe_allow_html=True)
