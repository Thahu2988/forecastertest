import streamlit as st
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide"
)

# --- Targeted CSS ---
hide_ui_css = """
<style>
/* --- Hide the "Manage app" tab (top-right black tab) --- */
div[data-testid="stAppViewerControlPanel"] {
    display: none !important;
    visibility: hidden !important;
}

/* --- Hide the bottom-right Streamlit status box (optional) --- */
[data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
}

/* --- Hide the Streamlit footer --- */
footer {
    display: none !important;
}

/* --- Hide the main menu (three dots) --- */
#MainMenu {
    display: none !important;
}

/* --- Hide the toolbar but DO NOT affect the sidebar toggle --- */
header [data-testid="stToolbar"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
}

/* --- Explicitly restore and pin the sidebar toggle (top-left arrow) --- */
button[title="Show sidebar"],
button[title="Hide sidebar"] {
    visibility: visible !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 0.6rem !important;
    left: 0.6rem !important;
    z-index: 10000 !important;
    background-color: white !important;
    border: 1px solid #ddd !important;
    border-radius: 6px !important;
    width: 32px !important;
    height: 32px !important;
}
</style>
"""

# Apply CSS
st.markdown(hide_ui_css, unsafe_allow_html=True)

# --- Main Page Content ---
st.title("🛠️ Maldives Meteorological Service Tools")
st.markdown("---")

st.markdown(
    """
    Welcome to the **Maldives Meteorological Service internal application suite**.
    
    Use the navigation menu on the left to access the available tools.
    """
)

st.markdown("---")

# --- Initialize and Display App Run Time ---
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

start_time = st.session_state.get('start_time', 'N/A')
st.caption(f"App running as of {start_time} (Time Zone: Malé, Maldives)")
