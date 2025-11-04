import streamlit as st
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Forecasters Tools",
    page_icon="🛠️",
    layout="wide"
)

# --- CSS: keep UI tidy but don't rely only on classnames ---
base_css = """
<style>
/* hide Streamlit footer */
footer { display: none !important; }

/* hide main menu if present */
#MainMenu { display: none !important; }

/* make sure our pinned sidebar button appears above everything */
._pinned_sidebar_override {
    visibility: visible !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 0.6rem !important;
    left: 0.6rem !important;
    z-index: 2147483647 !important; /* extreme z-index to be on top */
    background: white !important;
    border-radius: 6px !important;
    border: 1px solid rgba(0,0,0,0.08) !important;
    width: 36px !important;
    height: 36px !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.12) !important;
}

/* visually hide elements we explicitly remove via JS (fallback) */
._streamlit_hidden_by_script { display: none !important; visibility: hidden !important; }
</style>
"""

# --- JavaScript: robust removals & restoration using text matching + MutationObserver ---
# Explanation (short): 
# - removeManage() hides any container whose text contains "Manage app"
# - restoreSidebar() searches for many possible sidebar toggle buttons (by title, aria-label, text, icons),
#   pins and forces them visible with an overriding CSS class.
# - MutationObserver re-applies functions when DOM changes.
script_js = r"""
<script>
(function() {
  // Utility: test if element has visible text matching a phrase
  function containsVisibleText(node, phrase) {
    try {
      if (!node) return false;
      const txt = node.innerText || node.textContent || '';
      if (!txt) return false;
      return txt.trim().toLowerCase().includes(phrase.toLowerCase());
    } catch (e) {
      return false;
    }
  }

  // Hide any ancestor container (div) of an element that contains "Manage app"
  function removeManage() {
    // Walk through elements that may include "Manage app"
    const phrases = ['manage app', 'manage your app', 'manage'];
    // scan likely candidates first (buttons, links, spans, divs)
    const selectorCandidates = 'button, a, span, div, p, h1, h2, h3';
    document.querySelectorAll(selectorCandidates).forEach((el) => {
      try {
        if (el.offsetParent === null && el.clientHeight === 0 && el.clientWidth === 0) {
          // probably hidden already
        }
        if (containsVisibleText(el, 'manage app')) {
          // find a reasonable ancestor to hide (prefer nearest role or data-testid container)
          let anc = el.closest('div') || el.parentElement;
          // climb a few levels to hide the whole tab/panel but not unrelated content
          for (let i=0;i<6 && anc; i++) {
            // mark for hiding
            anc.classList.add('_streamlit_hidden_by_script');
            // If this ancestor seems to be a floating control (position fixed) stop climbing
            const st = window.getComputedStyle(anc);
            if (st && (st.position === 'fixed' || st.position === 'sticky' || st.zIndex !== 'auto')) break;
            anc = anc.parentElement;
          }
        }
      } catch (e) {
        // ignore individual errors
      }
    });

    // Also try to hide common id/testid-based containers if present
    const possibleSelect = [
      '[data-testid="stAppViewerControlPanel"]',
      '[data-testid="stStatusWidget"]',
      '[aria-label*="Manage app"]',
      '[title*="Manage app"]'
    ];
    possibleSelect.forEach(sel => {
      try {
        const el = document.querySelector(sel);
        if (el) el.classList.add('_streamlit_hidden_by_script');
      } catch (e) {}
    });
  }

  // Try to find a sidebar toggle button and pin/restore it
  function restoreSidebar() {
    // candidate selectors that have been observed across Streamlit versions
    const selCandidates = [
      'button[title*="Show sidebar"]',
      'button[title*="Hide sidebar"]',
      'button[aria-label*="sidebar"]',
      'button[aria-label*="Toggle"]',
      'button[title*="Toggle sidebar"]',
      'button[role="button"]'
    ];

    // First, try exact/likely selectors
    for (const sel of selCandidates) {
      try {
        const nodes = document.querySelectorAll(sel);
        for (const node of nodes) {
          // skip if node seems unrelated by checking innerText or child icons
          // mark and style it
          node.classList.add('_pinned_sidebar_override');
          // remove accidental 'display:none' or hidden attributes
          node.style.display = 'inline-flex';
          node.style.visibility = 'visible';
          node.style.opacity = '1';
          node.style.pointerEvents = 'auto';
        }
      } catch (e) {}
    }

    // As a fallback: find any button that looks like a left-arrow (svg path or contains '<' char)
    const allButtons = Array.from(document.querySelectorAll('button'));
    for (const b of allButtons) {
      try {
        // if it already has our class, skip
        if (b.classList && b.classList.contains('_pinned_sidebar_override')) continue;
        const inner = (b.innerText || '').trim().toLowerCase();
        const aria = (b.getAttribute && (b.getAttribute('aria-label') || '')).toLowerCase();
        const title = (b.title || '').toLowerCase();

        // heuristics: arrow-like SVG inside, or title/aria mentioning sidebar, or small button near top-left
        const hasSvgArrow = b.querySelector && b.querySelector('svg') && (b.querySelector('svg').innerHTML.match(/path|polyline|polygon|line/) ? true : false);
        const likelyByText = inner === '' || inner.length < 4; // small icon-only buttons
        const mentionsSidebar = aria.includes('sidebar') || title.includes('sidebar') || title.includes('show sidebar') || title.includes('hide sidebar');

        // If any heuristic positive, pin it
        if (hasSvgArrow || mentionsSidebar || (likelyByText && isNearTopLeft(b))) {
          b.classList.add('_pinned_sidebar_override');
          b.style.display = 'inline-flex';
          b.style.visibility = 'visible';
          b.style.pointerEvents = 'auto';
          b.style.zIndex = '2147483647';
        }
      } catch (e) {}
    }
  }

  // Helper: determines whether element is positioned near top-left of viewport
  function isNearTopLeft(el) {
    try {
      const rect = el.getBoundingClientRect();
      if (!rect) return false;
      return rect.top < 120 && rect.left < 200;
    } catch (e) {
      return false;
    }
  }

  // Apply fixes now
  function applyAll() {
    try {
      removeManage();
      restoreSidebar();
    } catch (e) {
      console.error('applyAll error', e);
    }
  }

  // Run immediately
  applyAll();

  // Re-apply periodically (fallback)
  const fallbackInterval = setInterval(applyAll, 1200);

  // Re-apply on DOM mutations so dynamic updates won't re-show the tab
  const mo = new MutationObserver((mutations) => {
    applyAll();
  });
  mo.observe(document.documentElement || document.body, {
    childList: true,
    subtree: true,
    attributes: true
  });

  // Clean-up on unload
  window.addEventListener('beforeunload', () => {
    clearInterval(fallbackInterval);
    mo.disconnect();
  });
})();
</script>
"""

# Inject CSS + JS
st.markdown(base_css + script_js, unsafe_allow_html=True)

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
