import streamlit as st

# Set the page configuration for the Home page
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide"
)

# --- Custom CSS to Hide UI Elements (Aggressive Final Fix) ---
# This CSS hides the top-right menu and the bottom-right "Manage app" link.
hide_streamlit_ui = """
<style>
/* 1. Hide the top-right three-dot menu (#MainMenu) and the Share/Star toolbar */
#MainMenu {visibility: hidden;}

/* Hides the Share, Star, Edit, and GitHub icons */
[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0px !important;
    position: fixed !important;
}

/* 2. Hide the main footer text */
footer {
    visibility: hidden;
    height: 0;
}

/* 3. Hide the status widget (often the "Manage app" container) by data-testid */
[data-testid="stStatusWidget"] {
    visibility: hidden !important; 
    display: none !important;
}

/* Aggressive selectors to catch the floating footer/deployment widget */
.st-emotion-cache-nahz7x, .st-emotion-cache-1g8i5q1 {
    visibility: hidden !important;
    display: none !important;
}

div[data-testid="stDecoration"] {
    visibility: hidden !important; 
    display: none !important;
}
</style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# --- Title and Introduction ---
st.title("🛠️ Maldives Meteorological Service Tools")
st.markdown("---")

st.markdown(
    """
    Welcome to the **Maldives Meteorological Service internal application suite**.
    
    Use the navigation menu on the left to access the available tools.
    """
)

# --- Tool Description Removed --- 
# The "Viber Forecast Generator" section was here and has been removed.

st.markdown("---")

start_time = st.session_state.get('start_time', 'N/A')
st.caption(f"App running as of {start_time}")
