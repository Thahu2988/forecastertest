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
/* Hide the "Manage app" black tab (top-right) */
div[data-testid="stAppViewerControlPanel"] {
    display: none !important;
    visibility: hidden !important;
}

/* Hide bottom-right status widget */
[data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
}

/* Hide Streamlit footer and main menu */
footer, #MainMenu {display: none !important;}

/* Hide Streamlit toolbar (Share, etc.) */
[data-testid="stToolbar"] {
    display: none !important;
    visibility: hidden !important;
}

/* Hide sidebar and its toggle */
section[data-testid="stSidebar"],
button[title="Toggle sidebar"],
button[title="Open sidebar"],
button[title="Hide sidebar"] {
    display: none !important;
}

/* --- Layout Styling --- */
body {
    background-color: #f8f9fa;
}

.header-container {
    text-align: center;
    padding-top: 2.5rem;
    padding-bottom: 0.5rem;
}

/* Button container (below title) */
.button-container {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 1rem;
    margin-bottom: 1.5rem;
}

/* Buttons */
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

# --- Header (Top Section) ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.title("🛠️ Maldives Meteorological Service Tools")

# --- Buttons just below title ---
st.markdown('<div class="button-container">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🌧️ Rainfall Outlook", key="rain"):
        st.switch_page("pages/Rainfall_Outlook.py")
with col2:
    if st.button("🌡️ Temperature Outlook", key="temp"):
        st.switch_page("pages/Temperature_Outlook.py")
st.markdown('</div>', unsafe_allow_html=True)

# --- Subtext ---
st.markdown('<p class="subtext">Select a forecast tool to begin</p>', unsafe_allow_html=True)

# --- Initialize and Display App Run Time ---
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f'<p class="caption">App running as of {st.session_state["start_time"]} (Time Zone: Malé, Maldives)</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
