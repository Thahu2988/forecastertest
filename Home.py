import streamlit as st

# Set the page configuration for the Home page
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide"
)

# --- START: Custom CSS to Hide UI Elements ---
hide_streamlit_ui = """
<style>
/* 1. Hide the top-right three-dot menu, Share, Star, Edit, and GitHub icons */
#MainMenu {visibility: hidden;}

/* This selector targets the toolbar that appears on hover (Share, Star, etc.) */
[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0px !important;
    position: fixed !important;
}

/* 2. Hide the "Manage app" link and Streamlit logo in the footer */
footer {
    visibility: hidden;
}

/* On deployed apps, this specifically targets the 'Manage app' button/container */
.st-emotion-cache-1j00l9g { 
    visibility: hidden !important; 
    display: none !important;
}

</style>
"""

st.markdown(hide_streamlit_ui, unsafe_allow_html=True)
# --- END: Custom CSS to Hide UI Elements ---


# --- Title and Introduction ---
st.title("🛠️ Maldives Meteorological Service Tools")
st.markdown("---")

# ... rest of your code ...
# (The rest of your script remains the same)
