import streamlit as st

# Set the page configuration for the Home page
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide"
)

# --- CSS to Hide Streamlit UI Components ---
# The target for the "Manage app" box is usually 'stStatusWidget' or the footer.
hide_streamlit_ui = """
<style>
/* 1. Hides the standard footer (which sometimes hosts similar info) */
footer {
    visibility: hidden !important;
    height: 0 !important;
    display: none !important;
}

/* 2. Hides the stStatusWidget (This is the primary target for the "Manage app" floating box) */
[data-testid="stStatusWidget"] {
    visibility: hidden !important;
    display: none !important;
}

/* 3. Hides the top-right menu and toolbar (Share, Star, Edit, three dots, etc.) for completeness */
#MainMenu, [data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0px !important;
    position: fixed !important;
    display: none !important; 
}

</style>
"""
# Apply the CSS using st.markdown with unsafe_allow_html=True
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

# Note: st.session_state must be initialized before accessing keys
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = 'N/A'

start_time = st.session_state.get('start_time')
st.caption(f"App running as of {start_time}")
