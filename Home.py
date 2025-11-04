import streamlit as st

# Set the page configuration for the Home page
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide"
)

# --- Ultra-Aggressive CSS to Hide All Deployment UI ---
hide_streamlit_ui = """
<style>
/* Hides the top-right menu and toolbar (Share, Star, Edit, GitHub, three dots) */
#MainMenu, [data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0px !important;
    position: fixed !important;
    display: none !important; 
}

/* Hides the standard footer text/logo */
footer {
    visibility: hidden !important;
    height: 0 !important;
    display: none !important;
}

/* Hides the stStatusWidget (often the "Manage app" container) by data-testid */
[data-testid="stStatusWidget"] {
    visibility: hidden !important; 
    display: none !important;
}

/* Targets the primary container for floating status/deployment UI */
div[data-testid="stDecoration"] {
    visibility: hidden !important;
    display: none !important;
}

/* Targets common classes for the floating bottom-right container */
.st-emotion-cache-1g8i5q1.e1nx5aiz1, .css-1g8i5q1, .st-emotion-cache-nahz7x {
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

st.markdown("---")

start_time = st.session_state.get('start_time', 'N/A')
st.caption(f"App running as of {start_time}")
