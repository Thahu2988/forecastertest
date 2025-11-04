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
/* --- Hide the Streamlit Cloud "Manage app" tab (top-right black tab) --- */
div[data-testid="stAppViewerControlPanel"] {
    display: none !important;
    visibility: hidden !important;
}

/* --- Hide the bottom-right status widget (optional) --- */
[data-testid="stStatusWidget"] {
    visibility: hidden !important;
    display: none !important;
}

/* --- Hide Streamlit's default footer --- */
footer {
    visibility: hidden !important;
    height: 0 !important;
    display: none !important;
}

/* --- Hide the main menu (top-right three dots) --- */
#MainMenu {
    visibility: hidden !important;
}

/* --- Hide Streamlit toolbar (Share, Edit, etc.) but keep sidebar toggle visible --- */
[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0 !important;
    display: none !important;
}

/* --- Ensure sidebar toggle (arrow / hamburger) remains visible --- */
button[kind="header"] {
    visibility: visible !important;
    display: flex !important;
    position: relative !important;
    z-index: 999 !important;
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
