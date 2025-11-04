import streamlit as st
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
<style>
/* Hide Streamlit Cloud "Manage app" tab */
div[data-testid="stAppViewerControlPanel"] {display: none !important;}
[data-testid="stStatusWidget"] {display: none !important;}
footer, #MainMenu {display: none !important;}
[data-testid="stToolbar"] {display: none !important;}

/* Center container */
.center-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 80vh;
    text-align: center;
}

/* Menu buttons */
.menu-button {
    background-color: #f0f2f6;
    color: #000;
    padding: 0.8em 2em;
    margin: 0.5em;
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
</style>
""", unsafe_allow_html=True)

# --- Main Page ---
st.markdown('<div class="center-container">', unsafe_allow_html=True)
st.title("🛠️ Maldives Meteorological Service Tools")
st.markdown("### Select a tool below")

# --- Central navigation menu ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌧️ Rainfall Outlook", key="rain"):
        st.switch_page("pages/Rainfall_Outlook.py")

    if st.button("🌡️ Temperature Outlook", key="temp"):
        st.switch_page("pages/Temperature_Outlook.py")

    if st.button("🏠 Home", key="home"):
        st.switch_page("Home.py")

st.markdown('</div>', unsafe_allow_html=True)

# --- Initialize and Display App Run Time ---
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

start_time = st.session_state.get('start_time', 'N/A')
st.caption(f"App running as of {start_time} (Time Zone: Malé, Maldives)")
