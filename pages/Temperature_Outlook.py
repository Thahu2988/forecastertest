import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import box
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib import colorbar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import io
import warnings

# Set the page configuration for the map tool
st.set_page_config(
    page_title="Rainfall Outlook Generator",
    page_icon="🗺️",
    layout="wide"
)

# --- Custom CSS to Control UI Elements ---
hide_streamlit_ui = """
<style>
/* 1. Hide the top-right Streamlit toolbar (Share, Star, Edit, etc.) */
#MainMenu {visibility: hidden;} /* Hides the three-dot menu */

[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0px !important;
    position: fixed !important;
}

/* 2. Hide the entire footer area, which contains the bottom-right elements */
footer {
    visibility: hidden !important;
    display: none !important; 
    height: 0px !important;
}

/* 3. Aggressively hide the specific container for 'Manage app' or similar bottom-right features */
.st-emotion-cache-1j00l9g, .st-emotion-cache-1fv82ss { 
    visibility: hidden !important; 
    display: none !important;
}

/* *** 4. FORCE THE TOP-LEFT SIDEBAR TOGGLE ARROW TO BE ALWAYS VISIBLE *** */

/* Targets the main button element by test ID */
[data-testid="stSidebarToggleButton"] {
    /* Critical: Override Streamlit's opacity and visibility rules */
    opacity: 1 !important; 
    visibility: visible !important; 
    display: flex !important; /* Use flex to ensure proper rendering */
    pointer-events: auto !important; /* Ensure it remains clickable */
}

/* Targets the internal icon element (the actual arrow image) for maximum aggression */
[data-testid="stSidebarToggleButton"] svg {
    visibility: visible !important;
    opacity: 1 !important;
}

/* Ensure the main content area has the space it needs */
section.main {
    padding-top: 5rem; 
}
</style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# --- Ignore harmless warnings ---
warnings.filterwarnings("ignore", message="missing ScriptRunContext")
warnings.filterwarnings("ignore", message="not compatible with tight_layout")

# --- Load shapefile ---
shp = 'data/Atoll_boundary2016.shp'
# NOTE: Added error handling in case the shapefile is missing
try:
    gdf = gpd.read_file(shp).to_crs(epsg=4326)
except Exception as e:
    st.error(f"Error loading shapefile: {e}. Please ensure 'data/Atoll_boundary2016.shp' is accessible.")
    st.stop()
    
bbox = box(71, -1, 75, 7.5)
gdf = gdf[gdf.intersects(bbox)]

# --- Default probabilities ---
default_probs = {
    'Haa Alifu Atoll': 65,
    'Haa Dhaalu Atoll': 70,
    'Noonu Atoll': 68,
    'Baa Atoll': 72,
    'Lhaviyani Atoll': 65,
    'Raa Atoll': 68,
    'Shaviyani Atoll': 70,
    'Kaafu Atoll': 75,
    'Alifu Alifu Atoll': 65,
    'Alifu Dhaalu Atoll': 70,
    'Vaavu Atoll': 68,
    'Meemu Atoll': 62,
    "Male' City": 75,
    'Faafu Atoll': 50,
    'Dhaalu Atoll': 52,
    'Thaa Atoll': 45,
    'Laamu Atoll': 55,
    'Gaafu Alifu Atoll': 64,
    'Gaafu Dhaalu Atoll': 62,
    'Gnaviyani Atoll': 65,
    'Seenu Atoll': 75
}

# --- Colormaps for categories ---
category_colors = {
    "Above Normal": ['#ffffff', '#ffed5c', '#ffb833', '#ff8f00', '#f15c00', '#e20000'],
    "Normal": ['#ffffff', '#b2df8a', '#6dc068', '#2d933e', '#006a2e', '#014723'],
    "Below Normal": ['#ffffff', '#c8c8ff', '#a6b6ff', '#8798f0', '#6c7be0', '#3c4fc2']
}

# --- Sidebar UI ---
st.sidebar.header("🎛️ Adjust Atoll Probabilities & Categories")
custom_title = st.sidebar.text_input(
    "📝 Map Title:",
    value="Maximum Temperature Outlook for OND 2025"
)

# User inputs per atoll
user_probs = {}
user_categories = {}
for atoll, default in default_probs.items():
    st.sidebar.markdown(f"**{atoll}**")
    user_probs[atoll] = st.sidebar.slider(f"{atoll} Probability", 0, 100, default, step=1)
    user_categories[atoll] = st.sidebar.selectbox(
        f"{atoll} Category",
        ["Above Normal", "Normal", "Below Normal"],
        index=1
    )

generate_map = st.sidebar.button("🗺️ Generate Map")

# --- Main Content Display Logic ---
if generate_map:
    # Logic runs only when the button is clicked
    gdf['prob'] = gdf['Name'].map(user_probs)
    gdf['category'] = gdf['Name'].map(user_categories)

    # --- Colormap setup ---
    bins = [0, 35, 45, 55, 65, 75, 100]
    norm = BoundaryNorm(bins, ncolors=len(bins)-1, clip=True)
    tick_positions = [35, 45, 55, 65, 75]
    tick_labels = ['35', '45', '55', '65', '75']

    # --- Plot map ---
    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot each atoll individually according to its category (skip empty)
    for cat, cmap_list in category_colors.items():
        subset = gdf[gdf['category'] == cat]
        if not subset.empty:
            cmap = ListedColormap(cmap_list)
            subset.plot(
                column='prob', cmap=cmap, norm=norm,
                edgecolor='black', linewidth=0.5, ax=ax
            )

    # Map settings
    ax.set_xlim(71, 75)
    ax.set_ylim(-1, 7.5)
    ax.set_xlabel("Longitude (°E)")
    ax.set_ylabel("Latitude (°N)")
    st.title(custom_title) # Display title in the main area
    ax.set_title(custom_title, fontsize=16)
    ax.set_xticks([71, 72, 73, 74, 75])
    ax.set_xticklabels(["71°E", "72°E", "73°E", "74°E", "75°E"])

    # --- Colorbars ---
    width = "40%"
    height = "2.5%"
    start_x = 0.05
    start_y = 0.1
    spacing = 0.09

    def make_cb(ax, cmap, title, offset):
        cax = inset_axes(ax, width=width, height=height, loc='lower left',
                          bbox_to_anchor=(start_x, start_y + offset, 1, 1),
                          bbox_transform=ax.transAxes, borderpad=0)
        cb = colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, boundaries=bins,
                                   ticks=tick_positions, spacing='uniform', orientation='horizontal')
        cb.set_ticklabels(tick_labels)
        cax.set_title(title, fontsize=10, pad=6)
        cb.ax.tick_params(labelsize=9, pad=2)

    make_cb(ax, ListedColormap(category_colors["Above Normal"]), "Above Normal", 2 * spacing)
    make_cb(ax, ListedColormap(category_colors["Normal"]), "Normal", spacing)
    make_cb(ax, ListedColormap(category_colors["Below Normal"]), "Below Normal", 0)

    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

    # --- Display map ---
    st.pyplot(fig)

    # --- Download button ---
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300, bbox_inches="tight")
    buf.seek(0)
    st.download_button(
        label="💾 Download Map Image (PNG)",
        data=buf,
        file_name="Temperature_Outlook_Map.png",
        mime="image/png"
    )

    st.success("✅ Map generated successfully!")
else:
    # Default message when button hasn't been clicked
    st.title(custom_title)
    st.info("👈 Adjust probabilities and categories for each atoll, edit map title, then click 'Generate Map'.")
