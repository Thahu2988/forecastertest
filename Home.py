import streamlit as st

# Set the page configuration for the Home page
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide"
)

# --- Custom CSS to Hide UI Elements (More Robust) ---
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

/* 2. Hide the "Manage app" and Streamlit branding in the footer */
footer {
    visibility: hidden;
}

/* New: Targets the main status widget which often contains the "Manage app" button */
/* This is a common selector for the deployment-related controls */
[data-testid="stStatusWidget"] {
    visibility: hidden !important; 
    display: none !important;
}

/* Fallback for the dynamically generated class, which may have changed */
/* .st-emotion-cache-1j00l9g { 
    visibility: hidden !important; 
    display: none !important;
} */

</style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# --- Title and Introduction ---
st.title("🛠️ Maldives Meteorological Service Tools")
st.markdown("---")

st.markdown(
    """
    Welcome to the Maldives Meteorological Service internal application suite.
    
    Use the navigation menu on the left to access the available tools.
    """
)

# --- Tool Description ---
st.header("📲 Viber Forecast Generator")
st.info(
    """
    Navigate to the **Viber Forecast Tool** page (in the sidebar on the left) 
    to generate the daily weather post for social media and Viber channels.
    
    The tool allows you to input forecast text in both English and Dhivehi, 
    preview the graphic with correct fonts and images, and download the final image.
    
    ***
    
    ### 🛑 Important: Setup Check
    
    For the fonts and images to display and for the download function to work, 
    please ensure you have the following folder structure and config file at your project's root:
    
    1.  **`.streamlit/config.toml`** file exists with `[server] enableStaticServing = true`.
    2.  **`static/`** folder exists and contains all required assets (`.png` and `.ttf` files).
    """
)

st.markdown("---")

start_time = st.session_state.get('start_time', 'N/A')
st.caption(f"App running as of {start_time}")
