import streamlit as st
import datetime

# Set the page configuration for the Home page
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide"
)

# --- Targeted CSS to Hide ONLY the Deployment UI ---
hide_deployment_ui = """
<style>
/* 1. Primary target: Hides the "Manage app" floating box by its data-testid */
[data-testid="stStatusWidget"] {
    visibility: hidden !important;
    display: none !important;
}

/* 2. Secondary target: Hides the standard footer text/logo (often 'Made with Streamlit') */
footer {
    visibility: hidden !important;
    height: 0 !important;
    display: none !important;
}

/* 3. Optional: Hides the top-right menu (three dots, Share, etc.) */
#MainMenu {
    visibility: hidden !important;
}

/* 4. Optional: Hides the top toolbar (Edit, GitHub, etc.). 
   This selector is safe and does not affect the sidebar toggle. */
[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0px !important;
    position: fixed !important;
    display: none !important; 
}

/* IMPORTANT FIX: We REMOVED the overly aggressive selectors like:
   .st-emotion-cache-1g8i5q1.e1nx5aiz1, .css-1g8i5q1, .st-emotion-cache-nahz7x 
   These were likely hiding the sidebar toggle or other essential components. */

</style>
"""
# Apply the CSS
st.markdown(hide_deployment_ui, unsafe_allow_html=True)

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

# --- Initialize and Display App Run Time ---
# Initialize start_time if it doesn't exist, using the current time
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

start_time = st.session_state.get('start_time', 'N/A')
st.caption(f"App running as of {start_time} (Time Zone: Malé, Maldives)")
