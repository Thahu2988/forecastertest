import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import box
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib import colorbar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import streamlit as st
from io import BytesIO

# -------------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------------
st.set_page_config(
    page_title="Rainfall Outlook Generator",
    page_icon="🗺️",
    layout="wide"
)

# -------------------------------------------------------------
# AGGRESSIVE CSS TO HIDE STREAMLIT UI + MANAGE APP BAR
# -------------------------------------------------------------
hide_streamlit_ui = """
<style>
/* --- GLOBAL HIDE FOR TOP TOOLBAR, FOOTER, AND "MANAGE APP" --- */
header, footer, [data-testid="stStatusWidget"], [data-testid="stDecoration"],
[data-testid="stBottomBlock"], [data-testid="stSidebarFooter"],
[data-testid="stStatusWidgetContainer"], [data-testid="stToolbar"],
[data-testid="stAppViewerControlPanel"], [data-testid="stBottom"],
#MainMenu, .st-emotion-cache-12fmufv, .st-emotion-cache-z5fcl4,
.st-emotion-cache-n9h0v5, .st-emotion-cache-1j00l9g, .st-emotion-cache-1fv82ss {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    min-height: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    opacity: 0 !important;
    pointer-events: none !important;
}

/* --- EXPAND MAIN AREA TO FULL WIDTH --- */
.main .block-container {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
    max-width: 100% !important;
    width: 100% !important;
}
</style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# -------------------------------------------------------------
# LOAD SHAPEFILE
# -------------------------------------------------------------
shp = 'data/Atoll_boundary2016.shp'
try:
    gdf = gpd.read_file(shp).to_crs(epsg=4326)
except Exception as e:
    st.error(f"Error loading shapefile: {e}. Please ensure 'data/Atoll_boundary2016.shp' exists.")
    st.stop()

bbox = box(71, -1, 75, 7.5)
gdf = gdf[gdf.intersects(bbox)]

# -------------------------------------------------------------
# CLEANUP
# -------------------------------------------------------------
gdf['Name'] = gdf['Name'].fillna("Unknown")
unique_atolls = sorted(gdf['Name'].unique().tolist())

# -------------------------------------------------------------
# SIDEBAR INPUTS
# -------------------------------------------------------------
st.sidebar.markdown('### Adjust Atoll Categories & Percentages')
map_title = st.sidebar.text_input("Edit Map Title:", "Maximum Rainfall Outlook for OND 2025")

categories = ['Below Normal', 'Normal', 'Above Normal']
selected_categories = {}
selected_percentages = {}

for i, atoll in enumerate(unique_atolls):
    with st.sidebar.container(border=True):
        st.write(f"**{atoll}**")
        selected = st.selectbox("Category", categories, index=1, key=f"{atoll}_cat_{i}", label_visibility="collapsed")
        percent = st.slider("Probability (%)", min_value=0, max_value=100, value=60, step=5, key=f"{atoll}_perc_{i}")
        selected_categories[atoll] = selected
        selected_percentages[atoll] = percent

# -------------------------------------------------------------
# COLOR MAPS
# -------------------------------------------------------------
cmap_below = ListedColormap(['#ffffff', '#ffed5c', '#ffb833', '#ff8f00', '#f15c00', '#e20000'])
cmap_normal = ListedColormap(['#ffffff', '#b2df8a', '#6dc068', '#2d933e', '#006a2e', '#014723'])
cmap_above = ListedColormap(['#ffffff', '#c8c8ff', '#a6b6ff', '#8798f0', '#6c7be0', '#3c4fc2'])

bins = [0, 35, 45, 55, 65, 75, 100]
norm = BoundaryNorm(bins, ncolors=len(bins)-1, clip=True)
tick_positions = [35, 45, 55, 65, 75]
tick_labels = ['35', '45', '55', '65', '75']

# -------------------------------------------------------------
# APPLY SELECTIONS TO GDF
# -------------------------------------------------------------
gdf['category'] = gdf['Name'].map(selected_categories)
gdf['prob'] = gdf['Name'].map(selected_percentages)

# -------------------------------------------------------------
# PLOT MAP
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 10))

for cat, cmap in zip(['Below Normal', 'Normal', 'Above Normal'],
                     [cmap_below, cmap_normal, cmap_above]):
    subset = gdf[gdf['category'] == cat]
    if not subset.empty:
        subset.plot(column='prob', cmap=cmap, norm=norm,
                    edgecolor='black', linewidth=0.5, ax=ax)

ax.set_xlim(71, 75)
ax.set_ylim(-1, 7.5)
ax.set_title(map_title, fontsize=18)
ax.set_xlabel("Longitude (°E)", fontsize=14)
ax.set_ylabel("Latitude (°N)", fontsize=14)
ax.set_xticks([71, 72, 73, 74, 75])
ax.set_xticklabels(['71', '72', '73', '74', '75'])
ax.tick_params(labelsize=12)

# -------------------------------------------------------------
# COLORBARS
# -------------------------------------------------------------
width, height, start_x, start_y, spacing = "40%", "2.5%", 0.05, 0.1, 0.09

def make_cb(ax, cmap, title, offset):
    cax = inset_axes(ax, width=width, height=height, loc='lower left',
                     bbox_to_anchor=(start_x, start_y + offset, 1, 1),
                     bbox_transform=ax.transAxes, borderpad=0)
    cb = colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, boundaries=bins,
                               ticks=tick_positions, spacing='uniform', orientation='horizontal')
    cb.set_ticklabels(tick_labels)
    cax.set_title(title, fontsize=10, pad=6)
    cb.ax.tick_params(labelsize=9, pad=2)

make_cb(ax, cmap_above, "Above Normal", 2 * spacing)
make_cb(ax, cmap_normal, "Normal", spacing)
make_cb(ax, cmap_below, "Below Normal", 0)

plt.tight_layout()

# -------------------------------------------------------------
# DISPLAY AND DOWNLOAD
# -------------------------------------------------------------
buf = BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight')
buf.seek(0)

st.pyplot(fig)

st.download_button(
    label="Download Map as PNG",
    data=buf,
    file_name='rainfall_outlook_map.png',
    mime='image/png'
)
