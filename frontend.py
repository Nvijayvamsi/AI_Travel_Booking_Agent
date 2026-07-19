# import os
# import streamlit as st
# from datetime import datetime
# from langchain_core.messages import HumanMessage
# from main import app

# st.set_page_config(
#     page_title="AI Travel Booking System",
#     page_icon="✈️",
#     layout="wide"
# )

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

# html, body, .stApp {
#     font-family: 'Inter', sans-serif;
#     background-color: #080d14;
# }

# /* ── Hero ── */
# .hero-wrapper {
#     position: relative;
#     border-radius: 20px;
#     overflow: hidden;
#     margin-bottom: 2rem;
#     height: 280px;
# }
# .hero-bg {
#     width: 100%;
#     height: 100%;
#     object-fit: cover;
#     display: block;
#     filter: brightness(0.35);
#     position: absolute;
#     top: 0; left: 0;
# }
# .hero-content {
#     position: relative;
#     z-index: 2;
#     height: 100%;
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     justify-content: center;
#     text-align: center;
#     padding: 2rem;
# }
# .hero-badge {
#     background: rgba(58,123,213,0.25);
#     border: 1px solid rgba(58,123,213,0.5);
#     color: #7ab8f5 !important;
#     font-size: 0.75rem;
#     font-weight: 600;
#     letter-spacing: 0.12em;
#     text-transform: uppercase;
#     padding: 0.3rem 0.9rem;
#     border-radius: 20px;
#     margin-bottom: 0.9rem;
#     display: inline-block;
# }
# .hero-title {
#     font-size: 2.6rem;
#     font-weight: 700;
#     color: #ffffff;
#     margin: 0 0 0.6rem;
#     line-height: 1.2;
# }
# .hero-sub {
#     color: #94adc8;
#     font-size: 1rem;
#     max-width: 560px;
# }

# /* ── Input card ── */
# .input-card {
#     background: #0e1623;
#     border: 1px solid #1e2e44;
#     border-radius: 16px;
#     padding: 1.6rem 1.8rem;
#     margin-bottom: 1.5rem;
# }
# .input-label {
#     color: #7ab8f5;
#     font-size: 0.8rem;
#     font-weight: 600;
#     letter-spacing: 0.1em;
#     text-transform: uppercase;
#     margin-bottom: 0.5rem;
# }

# /* ── Quick destinations ── */
# .dest-row {
#     display: flex;
#     gap: 0.5rem;
#     flex-wrap: wrap;
#     margin: 0.8rem 0 1.2rem;
# }
# .dest-chip {
#     background: #111b2b;
#     border: 1px solid #1e3050;
#     color: #f7fdf4;
#     padding: 0.35rem 0.85rem;
#     border-radius: 20px;
#     font-size: 0.82rem;
#     cursor: pointer;
#     transition: all 0.2s;
# }
# .dest-chip:hover { background: #1a2e47; border-color: #3a7bd5; color: #fff; }

# /* ── Generate button ── */
# div[data-testid="stButton"] > button {
#     background: linear-gradient(135deg, #1a6bbf 0%, #0d4a8a 50%, #0a3d75 100%) !important;
#     color: #ffffff !important;
#     border: none !important;
#     border-radius: 12px !important;
#     padding: 0.85rem 2.5rem !important;
#     font-size: 1.05rem !important;
#     font-weight: 700 !important;
#     letter-spacing: 0.03em !important;
#     width: 100% !important;
#     box-shadow: 0 0 24px rgba(26,107,191,0.35), 0 4px 15px rgba(0,0,0,0.4) !important;
#     transition: all 0.3s ease !important;
# }
# div[data-testid="stButton"] > button:hover {
#     box-shadow: 0 0 40px rgba(26,107,191,0.6), 0 6px 20px rgba(0,0,0,0.5) !important;
#     transform: translateY(-2px) !important;
#     background: linear-gradient(135deg, #2278d4 0%, #1057a0 50%, #0d4a8a 100%) !important;
# }
# div[data-testid="stButton"] > button:active {
#     transform: translateY(0px) !important;
# }

# /* ── Agent status cards ── */
# [data-testid="stStatusWidget"] {
#     background: #0e1a2e !important;
#     border: 1px solid #1e3050 !important;
#     border-radius: 12px !important;
# }
# [data-testid="stStatusWidget"] > div:first-child {
#     background: #0e1a2e !important;
#     border-radius: 12px 12px 0 0 !important;
# }
# [data-testid="stStatusWidget"] details,
# [data-testid="stStatusWidget"] details > div,
# [data-testid="stStatusWidget"] [data-testid="stVerticalBlock"] {
#     background: #0a1520 !important;
#     color: #ffffff !important;
#     padding: 0.25rem 0.5rem !important;
# }
# [data-testid="stStatusWidget"] * { color: #ffffff !important; }
# [data-testid="stStatusWidget"] a { color: #4ea8f0 !important; }
# [data-testid="stStatusWidget"] hr { border-color: #1e3050 !important; }

# /* ── Section headers ── */
# .sec-head {
#     display: flex;
#     align-items: center;
#     gap: 0.6rem;
#     margin: 2rem 0 0.75rem;
#     padding-bottom: 0.5rem;
#     border-bottom: 1px solid #1e2e44;
# }
# .sec-head span { font-size: 1.15rem; font-weight: 600; color: #e0edf8; }

# /* ── Metric bar ── */
# .metric-row {
#     display: flex;
#     gap: 1rem;
#     margin: 1.5rem 0;
# }
# .metric-box {
#     flex: 1;
#     background: #0e1623;
#     border: 1px solid #1e2e44;
#     border-radius: 12px;
#     padding: 1rem 1.2rem;
#     text-align: center;
# }
# .metric-val { font-size: 1.8rem; font-weight: 700; color: #4ea8f0; }
# .metric-lbl { font-size: 0.78rem; color: #5a7a96; margin-top: 0.2rem; text-transform: uppercase; letter-spacing: 0.08em; }

# /* ── Final plan ── */
# .final-card {
#     background: linear-gradient(160deg, #0c1a2e 0%, #0a1520 100%);
#     border: 1px solid #1e3a5c;
#     border-left: 4px solid #3a7bd5;
#     border-radius: 14px;
#     padding: 1.8rem;
#     line-height: 1.8;
#     color: #cce0f5;
#     font-size: 0.95rem;
# }

# /* ── Save bar ── */
# .save-bar {
#     background: #0e1623;
#     border: 1px solid #1e2e44;
#     border-radius: 10px;
#     padding: 0.85rem 1.2rem;
#     color: #5a8ab0;
#     font-size: 0.88rem;
#     margin-top: 0.5rem;
# }

# /* ── Sidebar ── */
# section[data-testid="stSidebar"] {
#     background: #090e18 !important;
#     border-right: 1px solid #141f30 !important;
# }
# .sidebar-chip {
#     background: #0e1a2b;
#     border: 1px solid #1a2e44;
#     border-radius: 8px;
#     padding: 0.45rem 0.75rem;
#     margin-bottom: 0.4rem;
#     font-size: 0.83rem;
#     color: #7aa8cc;
# }
# .sidebar-title { color: #e0edf8; font-size: 1rem; font-weight: 600; margin: 1rem 0 0.5rem; }

# /* Hide branding */
# #MainMenu, footer, header { visibility: hidden; }

# /* Textarea */
# .stTextArea textarea {
#     background: #0a1520 !important;
#     border: 1px solid #1e2e44 !important;
#     border-radius: 10px !important;
#     color: #e8f4ff !important;
#     font-size: 0.95rem !important;
#     resize: none !important;
# }
# .stTextArea textarea:focus {
#     border-color: #3a7bd5 !important;
#     box-shadow: 0 0 0 2px rgba(58,123,213,0.2) !important;
# }
# .stTextArea textarea::placeholder { color: #4a6a85 !important; }

# /* Text input (sidebar User ID field) */
# input[type="text"], .stTextInput input {
#     background: #0e1a2b !important;
#     border: 1px solid #1a2e44 !important;
#     border-radius: 8px !important;
#     color: #e0edf8 !important;
# }
# input[type="text"]:focus, .stTextInput input:focus {
#     border-color: #3a7bd5 !important;
#     box-shadow: 0 0 0 2px rgba(58,123,213,0.2) !important;
# }
# input[type="text"]::placeholder { color: #3a5570 !important; }

# /* All Streamlit labels — dark bg → light text */
# .stTextInput label, .stTextArea label,
# .stSelectbox label, .stNumberInput label {
#     color: #7ab8f5 !important;
#     font-size: 0.82rem !important;
#     font-weight: 600 !important;
#     letter-spacing: 0.08em !important;
# }

# /* General markdown / paragraph text */
# .stMarkdown p, .stMarkdown li, .stMarkdown td, .stMarkdown th {
#     color: #cce0f5 !important;
# }
# .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: #e8f4ff !important; }
# .stMarkdown code {
#     background: #0e1a2b !important;
#     color: #7ab8f5 !important;
#     padding: 0.15em 0.4em;
#     border-radius: 4px;
# }

# /* Metric labels — was #5a7a96 (too dim on dark bg) */
# .metric-lbl { color: #7aa8cc !important; }

# /* Save bar — was #5a8ab0 (slightly dim) */
# .save-bar { color: #8ab8d8 !important; }
# .save-bar code { color: #7ab8f5 !important; background: #0a1520 !important; }

# /* Streamlit warning / info / success on dark bg */
# .stAlert { background: #0e1a2b !important; border-radius: 10px !important; }
# .stAlert p, .stAlert div { color: #e0edf8 !important; }

# /* Sidebar text & dividers */
# section[data-testid="stSidebar"] p,
# section[data-testid="stSidebar"] span,
# section[data-testid="stSidebar"] label,
# section[data-testid="stSidebar"] .stMarkdown { color: #a0c4e0 !important; }
# section[data-testid="stSidebar"] hr { border-color: #1a2e44 !important; }

# /* Download button — light bg → dark text  */
# div[data-testid="stDownloadButton"] > button {
#     background: #1a3a5c !important;
#     color: #e8f4ff !important;
#     border: 1px solid #2a5080 !important;
#     border-radius: 10px !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # ── Sidebar ───────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.markdown("<div class='sidebar-title'>🌍 AI Travel Planner</div>", unsafe_allow_html=True)
#     st.markdown("---")

#     thread_id = st.text_input("👤 User ID", value="aarohi_user",
#                               help="Your session ID — keeps travel history across queries")

#     st.markdown("<div class='sidebar-title'>Powered by</div>", unsafe_allow_html=True)
#     for tech in ["🔗 LangGraph", "🧠 Groq · LLaMA 3.3 70B", "🐘 PostgreSQL", "🔍 Tavily Search", "✈️ AviationStack"]:
#         st.markdown(f"<div class='sidebar-chip'>{tech}</div>", unsafe_allow_html=True)

#     st.markdown("<div class='sidebar-title'>Agent Pipeline</div>", unsafe_allow_html=True)
#     for step in ["① Flight Agent", "② Hotel Agent", "③ Itinerary Agent", "④ Final Agent"]:
#         st.markdown(f"<div class='sidebar-chip'>{step}</div>", unsafe_allow_html=True)

# # ── Hero ──────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero-wrapper">
#     <img class="hero-bg"
#          src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1400&q=80"
#          alt="airplane above clouds"/>
#     <div class="hero-content">
#         <div class="hero-badge">✦ Multi-Agent AI System</div>
#         <div class="hero-title">✈️ AI Travel Booking System</div>
#         <div class="hero-sub">Four specialized agents work together — searching flights, hotels, building an itinerary, and delivering your perfect trip plan.</div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # ── Destination image strip ───────────────────────────────────────────────────
# DESTINATIONS = [
#     ("🇯🇵 Tokyo",     "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=300&q=70"),
#     ("🇫🇷 Paris",     "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=300&q=70"),
#     ("🇹🇭 Bangkok",   "https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=300&q=70"),
#     ("🇮🇹 Rome",      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=300&q=70"),
#     ("🇦🇪 Dubai",     "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=300&q=70"),
# ]

# cols = st.columns(5)
# for col, (name, img_url) in zip(cols, DESTINATIONS):
#     with col:
#         st.markdown(f"""
#         <div style="border-radius:10px;overflow:hidden;position:relative;height:90px;cursor:pointer;">
#             <img src="{img_url}" style="width:100%;height:100%;object-fit:cover;filter:brightness(0.55);" />
#             <div style="position:absolute;bottom:8px;left:0;right:0;text-align:center;
#                         color:#fff;font-size:0.8rem;font-weight:600;">{name}</div>
#         </div>
#         """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # ── Input ─────────────────────────────────────────────────────────────────────
# st.markdown("<div class='input-label'>🗺️ Describe your trip</div>", unsafe_allow_html=True)

# QUICK = ["7-day Japan under ₹2L", "Paris trip for 5 days", "Dubai weekend trip", "Bali backpacking 10 days"]
# qcols = st.columns(len(QUICK))
# quick_fill = ""
# for qc, label in zip(qcols, QUICK):
#     with qc:
#         if st.button(label, key=f"q_{label}"):
#             quick_fill = label

# user_query = st.text_area(
#     "",
#     value=quick_fill,
#     placeholder="e.g. Plan a complete 7-day Japan trip including flights, hotels and sightseeing under ₹2 lakhs",
#     height=100,
#     label_visibility="collapsed",
# )

# generate = st.button("🚀  Generate My Travel Plan", use_container_width=True)

# # ── Agent pipeline ────────────────────────────────────────────────────────────
# AGENT_META = {
#     "flight_agent":    ("✈️", "Flight Agent"),
#     "hotel_agent":     ("🏨", "Hotel Agent"),
#     "itinerary_agent": ("🗓️", "Itinerary Agent"),
#     "final_agent":     ("🧠", "Final Agent"),
# }

# if generate:
#     if not user_query.strip():
#         st.warning("Please describe your trip first.")
#     else:
#         config = {"configurable": {"thread_id": thread_id}}
#         collected = {"flight_results": "", "hotel_results": "",
#                      "itinerary": "", "final_response": "", "llm_calls": 0}

#         st.markdown("---")
#         st.markdown("<div class='sec-head'><span>🤖 Agent Pipeline — Live</span></div>",
#                     unsafe_allow_html=True)

#         for chunk in app.stream(
#             {
#                 "messages": [HumanMessage(content=user_query)],
#                 "user_query": user_query,
#                 "flight_results": "",
#                 "hotel_results": "",
#                 "itinerary": "",
#                 "llm_calls": 0,
#             },
#             config=config,
#             stream_mode="updates",
#         ):
#             for node_name, state_update in chunk.items():
#                 icon, label = AGENT_META.get(node_name, ("🔧", node_name))

#                 with st.status(f"{icon}  {label}", state="complete", expanded=True):
#                     if node_name == "flight_agent":
#                         text = state_update.get("flight_results", "")
#                         collected["flight_results"] = text
#                         st.markdown(text or "_No flight data returned._")

#                     elif node_name == "hotel_agent":
#                         text = state_update.get("hotel_results", "")
#                         collected["hotel_results"] = text
#                         st.markdown(text or "_No hotel data returned._")

#                     elif node_name == "itinerary_agent":
#                         text = state_update.get("itinerary", "")
#                         collected["itinerary"] = text
#                         st.markdown(text or "_No itinerary generated._")

#                     elif node_name == "final_agent":
#                         msgs = state_update.get("messages", [])
#                         text = msgs[-1].content if msgs else ""
#                         collected["final_response"] = text
#                         st.markdown(text or "_No final response._")

#                     collected["llm_calls"] = state_update.get("llm_calls", collected["llm_calls"])

#         # Metrics
#         st.markdown(f"""
#         <div class="metric-row">
#             <div class="metric-box"><div class="metric-val">4</div><div class="metric-lbl">Agents Run</div></div>
#             <div class="metric-box"><div class="metric-val">{collected['llm_calls']}</div><div class="metric-lbl">LLM Calls</div></div>
#             <div class="metric-box"><div class="metric-val">✅</div><div class="metric-lbl">Status</div></div>
#         </div>
#         """, unsafe_allow_html=True)

#         # Final plan card
#         if collected["final_response"]:
#             st.markdown("<div class='sec-head'><span>🧠 Final Travel Plan</span></div>",
#                         unsafe_allow_html=True)
#             st.markdown(f"<div class='final-card'>{collected['final_response']}</div>",
#                         unsafe_allow_html=True)

#         # Save
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"travel_plan_{timestamp}.md"
#         save_dir = os.path.join(os.path.dirname(__file__), "travel_plans")
#         os.makedirs(save_dir, exist_ok=True)

#         file_content = f"""# Travel Plan
# **Query:** {user_query}
# **Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# **User ID:** {thread_id}

# ---

# ## ✈️ Flight Information
# {collected['flight_results'] or 'N/A'}

# ---

# ## 🏨 Hotel Information
# {collected['hotel_results'] or 'N/A'}

# ---

# ## 🗓️ Itinerary
# {collected['itinerary'] or 'N/A'}

# ---

# ## 🧠 Final Travel Plan
# {collected['final_response'] or 'N/A'}

# ---
# *LLM Calls: {collected['llm_calls']}*
# """
#         with open(os.path.join(save_dir, filename), "w", encoding="utf-8") as f:
#             f.write(file_content)

#         dl_col, info_col = st.columns([1, 3])
#         with dl_col:
#             st.download_button("⬇️ Download Plan", data=file_content,
#                                file_name=filename, mime="text/markdown",
#                                use_container_width=True)
#         with info_col:
#             st.markdown(f"<div class='save-bar'>📁 Auto-saved → <code>travel_plans/{filename}</code></div>",
#                         unsafe_allow_html=True)

import os
import streamlit as st
from datetime import datetime
from langchain_core.messages import HumanMessage

# Demo mode guard: if `DEMO_MODE` is truthy we avoid importing `main`
# because `main` requires a configured `DATABASE_URL` and external LLMs.
DEMO_MODE = os.getenv("DEMO_MODE", "false").lower() in ("1", "true", "yes")
app = None
_import_error = None
if not DEMO_MODE:
    try:
        from main import app as app
    except Exception as e:
        # Keep going in a degraded mode; frontend will show a warning.
        _import_error = e

st.set_page_config(
    page_title="AI Travel Booking System",
    page_icon="✈️",
    layout="wide"
)

# ── Theme Configuration & Dynamic CSS ─────────────────────────────────────────
# Sidebar Theme Selector
with st.sidebar:
    st.markdown("<h3 style='margin-bottom:0px; padding-bottom:0px;'>🎨 Customize App</h3>", unsafe_allow_html=True)
    theme_choice = st.selectbox(
        "Select Visual Theme",
        options=["Midnight Dark 🌌", "Elysian Light ☀️"],
        index=0
    )

# Establish styling bases for Light and Dark modes
if "Midnight Dark" in theme_choice:
    bg_color = "#070c14"
    card_bg = "#0e1726"
    card_border = "#1f314d"
    text_primary = "#f0f5fc"
    text_secondary = "#8fa3be"
    accent = "#3a86ff"
    accent_glow = "rgba(58, 134, 255, 0.45)"
    metric_bg = "#111c2e"
    sidebar_bg = "#090f19"
    input_bg = "#0a101a"
    hero_grad = "linear-gradient(135deg, rgba(13,27,42,0.9) 0%, rgba(11,19,30,0.95) 100%)"
else: # Elysian Light Mode
    bg_color = "#f4f7fc"
    card_bg = "#ffffff"
    card_border = "#dbe3f0"
    text_primary = "#1e293b"
    text_secondary = "#64748b"
    accent = "#1a6bbf"
    accent_glow = "rgba(26, 107, 191, 0.25)"
    metric_bg = "#f0f4fa"
    sidebar_bg = "#ffffff"
    input_bg = "#f8fafc"
    hero_grad = "linear-gradient(135deg, rgba(224,236,250,0.85) 0%, rgba(240,245,253,0.9) 100%)"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body, .stApp {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: {bg_color} !important;
    color: {text_primary} !important;
    transition: all 0.3s ease;
}}

/* ── Hero section ── */
.hero-wrapper {{
    position: relative;
    border-radius: 24px;
    overflow: hidden;
    margin-bottom: 2rem;
    height: 320px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}}
.hero-bg {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    position: absolute;
    top: 0; left: 0;
    z-index: 1;
}}
.hero-overlay {{
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: {hero_grad};
    backdrop-filter: blur(3px);
    z-index: 2;
}}
.hero-content {{
    position: relative;
    z-index: 3;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 2rem;
}}
.hero-badge {{
    background: {accent_glow};
    border: 1px solid {accent};
    color: {accent} !important;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 0.4rem 1.1rem;
    border-radius: 50px;
    margin-bottom: 1rem;
    display: inline-block;
    box-shadow: 0 4px 12px {accent_glow};
}}
.hero-title {{
    font-size: 3rem;
    font-weight: 800;
    color: {text_primary};
    margin: 0 0 0.8rem;
    line-height: 1.1;
    letter-spacing: -0.02em;
}}
.hero-sub {{
    color: {text_secondary};
    font-size: 1.1rem;
    max-width: 650px;
}}

/* ── Destination Cards with Zoom & Hover animations ── */
.dest-card {{
    border-radius: 16px;
    overflow: hidden;
    position: relative;
    height: 130px;
    cursor: pointer;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.4s;
}}
.dest-card:hover {{
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 12px 30px {accent_glow};
}}
.dest-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}}
.dest-card:hover .dest-img {{
    transform: scale(1.15);
}}
.dest-overlay {{
    position: absolute;
    bottom: 0; left: 0; right: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.3) 70%, transparent 100%);
    padding: 1.5rem 0.75rem 0.75rem;
    text-align: center;
}}
.dest-name {{
    color: #ffffff !important;
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 0.05em;
}}

/* ── Form Container & Inputs ── */
.input-card-wrap {{
    background: {card_bg};
    border: 1px solid {card_border};
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
}}
.input-label {{
    color: {accent};
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}}

/* Custom styling for standard text-area input */
.stTextArea textarea {{
    background-color: {input_bg} !important;
    border: 1px solid {card_border} !important;
    border-radius: 14px !important;
    color: {text_primary} !important;
    font-size: 1rem !important;
    padding: 1rem !important;
    transition: border-color 0.3s, box-shadow 0.3s !important;
}}
.stTextArea textarea:focus {{
    border-color: {accent} !important;
    box-shadow: 0 0 0 3px {accent_glow} !important;
}}

/* ── Main Interactive Buttons ── */
div[data-testid="stButton"] > button {{
    background: linear-gradient(135deg, {accent} 0%, #10529d 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.9rem 2.5rem !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    box-shadow: 0 4px 20px {accent_glow} !important;
    transition: all 0.3s ease !important;
}}
div[data-testid="stButton"] > button:hover {{
    box-shadow: 0 8px 30px {accent_glow} !important;
    transform: translateY(-2px) !important;
    background: linear-gradient(135deg, #4d94ff 0%, {accent} 100%) !important;
}}
div[data-testid="stButton"] > button:active {{
    transform: translateY(0px) !important;
}}

/* Quick Prompt Chip Buttons */
div[data-element-id="stHorizontalBlock"] button {{
    background-color: {card_bg} !important;
    border: 1px solid {card_border} !important;
    color: {text_primary} !important;
    padding: 0.4rem 1rem !important;
    font-size: 0.85rem !important;
    border-radius: 30px !important;
    transition: all 0.2s ease !important;
    box-shadow: none !important;
}}
div[data-element-id="stHorizontalBlock"] button:hover {{
    background-color: {accent} !important;
    color: #ffffff !important;
    border-color: {accent} !important;
    transform: translateY(-1px) !important;
}}

/* ── Sidebar Styling ── */
section[data-testid="stSidebar"] {{
    background-color: {sidebar_bg} !important;
    border-right: 1px solid {card_border} !important;
}}
section[data-testid="stSidebar"] .stMarkdown {{
    color: {text_primary} !important;
}}
.sidebar-title {{
    color: {text_primary};
    font-size: 1.2rem;
    font-weight: 700;
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
}}
.sidebar-chip {{
    background: {metric_bg};
    border: 1px solid {card_border};
    border-radius: 10px;
    padding: 0.5rem 0.8rem;
    margin-bottom: 0.5rem;
    font-size: 0.85rem;
    color: {text_secondary};
    font-weight: 500;
}}

/* ── Live Agent Stream Widgets ── */
[data-testid="stStatusWidget"] {{
    background-color: {card_bg} !important;
    border: 1px solid {card_border} !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05) !important;
}}
[data-testid="stStatusWidget"] * {{
    color: {text_primary} !important;
}}

/* ── Metrics Panel ── */
.metric-row {{
    display: flex;
    gap: 1.25rem;
    margin: 1.8rem 0;
}}
.metric-box {{
    flex: 1;
    background: {metric_bg};
    border: 1px solid {card_border};
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    text-align: center;
    transition: transform 0.2s;
}}
.metric-box:hover {{
    transform: translateY(-3px);
}}
.metric-val {{
    font-size: 2.2rem;
    font-weight: 800;
    color: {accent};
}}
.metric-lbl {{
    font-size: 0.8rem;
    color: {text_secondary};
    margin-top: 0.4rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 600;
}}

/* ── Final Plan Card ── */
.final-card {{
    background: {card_bg};
    border: 1px solid {card_border};
    border-left: 6px solid {accent};
    border-radius: 18px;
    padding: 2.2rem;
    line-height: 1.85;
    color: {text_primary};
    font-size: 1rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
}}

/* ── Download & Save Elements ── */
div[data-testid="stDownloadButton"] > button {{
    background: {metric_bg} !important;
    color: {text_primary} !important;
    border: 1px solid {card_border} !important;
    border-radius: 12px !important;
    padding: 0.75rem 1.5rem !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    box-shadow: none !important;
}}
div[data-testid="stDownloadButton"] > button:hover {{
    background: {accent} !important;
    color: #ffffff !important;
    border-color: {accent} !important;
}}
.save-bar {{
    background: {metric_bg};
    border: 1px solid {card_border};
    border-radius: 12px;
    padding: 0.9rem 1.5rem;
    color: {text_secondary};
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}}
.save-bar code {{
    background: {card_bg} !important;
    color: {accent} !important;
    padding: 0.2rem 0.5rem;
    border-radius: 6px;
    border: 1px solid {card_border};
}}

/* Hidden default items */
#MainMenu, footer, header {{ visibility: hidden; }}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("---")
    st.markdown("<div class='sidebar-title'>🌍 Profile Configuration</div>", unsafe_allow_html=True)
    
    thread_id = st.text_input("👤 User Session ID", value="aarohi_user",
                             help="Your session ID — keeps travel history across queries")

    st.markdown("<div class='sidebar-title'>System Engine</div>", unsafe_allow_html=True)
    for tech in ["🔗 LangGraph Orchestration", "🧠 Groq · LLaMA 3.3 70B", "🐘 PostgreSQL Memory", "🔍 Tavily Web Search", "✈️ AviationStack Live API"]:
        st.markdown(f"<div class='sidebar-chip'>{tech}</div>", unsafe_allow_html=True)

    st.markdown("<div class='sidebar-title'>Active Pipeline Nodes</div>", unsafe_allow_html=True)
    for step in ["① Flight Intelligence Agent", "② Hospitality Search Agent", "③ Local Experience Planner", "④ Executive Synthesis Agent"]:
        st.markdown(f"<div class='sidebar-chip'>{step}</div>", unsafe_allow_html=True)

# ── Hero Section ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrapper">
    <img class="hero-bg"
         src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1400&q=80"
         alt="airplane above clouds"/>
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <div class="hero-badge">✦ High-Performance Multi-Agent System</div>
        <div class="hero-title">AI Travel Booking Platform</div>
        <div class="hero-sub">Engage an orchestra of collaborative AI agents trained to research flights, curate boutique hotels, map schedules, and tailor your dream trip.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Multi-Destination Dynamic Showreel (Indian & Foreign Highlights) ──────────
st.markdown("<div class='input-label' style='margin-bottom: 0.8rem;'>✨ Featured Destinations</div>", unsafe_allow_html=True)

DESTINATIONS = [
    ("🇮🇳 Agra, India", "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=300&q=80"),
    ("🇮🇳 Kerala, India", "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?w=300&q=80"),
    ("🇯🇵 Tokyo, Japan", "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=300&q=80"),
    ("🇫🇷 Paris, France", "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=300&q=80"),
    ("🇦🇪 Dubai, UAE", "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=300&q=80"),
]

cols = st.columns(5)
for col, (name, img_url) in zip(cols, DESTINATIONS):
    with col:
        st.markdown(f"""
        <div class="dest-card">
            <img class="dest-img" src="{img_url}" />
            <div class="dest-overlay">
                <div class="dest-name">{name}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Dynamic User Inputs ────────────────────────────────────────────────────────
st.markdown("<div class='input-label'>🗺️ Design Your Custom Journey</div>", unsafe_allow_html=True)

# Interactive Quick Prompt Chips
QUICK_PROMPTS = [
    "5-Day Heritage Tour of Agra & Jaipur under ₹75,000",
    "8-Day Relaxing Kerala Backwaters & Beaches Escapade",
    "7-Day Tokyo Lights & Kyoto Traditions under ₹2L",
    "Luxury Dubai Honeymoon Week"
]

qcols = st.columns(len(QUICK_PROMPTS))
quick_fill = ""
for qc, label in zip(qcols, QUICK_PROMPTS):
    with qc:
        if st.button(label, key=f"q_{label}"):
            quick_fill = label

user_query = st.text_area(
    "",
    value=quick_fill if quick_fill else "",
    placeholder="Describe your perfect trip in plain English (e.g., 'Plan an elegant 6-day family trip to Kerala staying in houseboats and resorts under ₹1.5L...'",
    height=110,
    label_visibility="collapsed",
)

generate = st.button("🚀  Generate Travel Dossier", use_container_width=True)

# ── Multi-Agent Streaming Pipeline Execution ──────────────────────────────────
AGENT_META = {
    "flight_agent":     ("✈️", "Flight Intelligence Agent"),
    "hotel_agent":      ("🏨", "Hospitality Search Agent"),
    "itinerary_agent":  ("🗓️", "Local Experience Planner"),
    "final_agent":      ("🧠", "Executive Synthesis Agent"),
}

if generate:
    if not user_query.strip():
        st.warning("Please provide a prompt or select a featured destination above to design your trip.")
    else:
        config = {"configurable": {"thread_id": thread_id}}
        collected = {"flight_results": "", "hotel_results": "",
                     "itinerary": "", "final_response": "", "llm_calls": 0}

        st.markdown("---")
        st.markdown("<h3 style='margin-bottom:1rem;'>🤖 Active Multi-Agent Pipeline Execution</h3>", unsafe_allow_html=True)

        if DEMO_MODE or app is None:
            if _import_error is not None:
                st.warning(f"Running in demo mode because importing the backend failed: {_import_error}")

            # Simple canned/demo outputs so UI can be verified without external services
            collected["flight_results"] = (
                "1. Airline: DemoAir\n   Departure: DEMO Airport A\n   Arrival: DEMO Airport B\n   Status: Scheduled"
            )
            collected["hotel_results"] = (
                "1. **Demo Hotel**\n   https://example.com/hotel\n   A comfortable demo stay in the city center."
            )
            collected["itinerary"] = (
                "Day 1: Arrival and city tour\nDay 2: Local experiences\nDay 3: Departure"
            )
            collected["final_response"] = (
                "Demo travel plan: 3-day sample itinerary including flights and hotels."
            )
            collected["llm_calls"] = 0

            st.markdown(f"<div class='sec-head'><span>🤖 Agent Pipeline — Demo</span></div>", unsafe_allow_html=True)
            for node_name in ["flight_agent", "hotel_agent", "itinerary_agent", "final_agent"]:
                icon, label = AGENT_META.get(node_name, ("🔧", node_name))
                with st.status(f"{icon}  {label}", state="complete", expanded=True):
                    if node_name == "flight_agent":
                        st.markdown(collected["flight_results"]) 
                    elif node_name == "hotel_agent":
                        st.markdown(collected["hotel_results"]) 
                    elif node_name == "itinerary_agent":
                        st.markdown(collected["itinerary"]) 
                    elif node_name == "final_agent":
                        st.markdown(collected["final_response"]) 
        else:
            for chunk in app.stream(
                {
                    "messages": [HumanMessage(content=user_query)],
                    "user_query": user_query,
                    "flight_results": "",
                    "hotel_results": "",
                    "itinerary": "",
                    "llm_calls": 0,
                },
                config=config,
                stream_mode="updates",
            ):
                for node_name, state_update in chunk.items():
                    icon, label = AGENT_META.get(node_name, ("🔧", node_name))

                    with st.status(f"{icon}  {label}", state="complete", expanded=True):
                        if node_name == "flight_agent":
                            text = state_update.get("flight_results", "")
                            collected["flight_results"] = text
                            st.markdown(text or "_No flight options found._")

                        elif node_name == "hotel_agent":
                            text = state_update.get("hotel_results", "")
                            collected["hotel_results"] = text
                            st.markdown(text or "_No accommodations discovered._")

                        elif node_name == "itinerary_agent":
                            text = state_update.get("itinerary", "")
                            collected["itinerary"] = text
                            st.markdown(text or "_No routing plan constructed._")

                        elif node_name == "final_agent":
                            msgs = state_update.get("messages", [])
                            text = msgs[-1].content if msgs else ""
                            collected["final_response"] = text
                            st.markdown(text or "_No unified response._")

                        collected["llm_calls"] = state_update.get("llm_calls", collected["llm_calls"])

        # Display Live Performance Metrics
        st.markdown(f"""
        <div class="metric-row">
            <div class="metric-box">
                <div class="metric-val">4</div>
                <div class="metric-lbl">Active Agents Run</div>
            </div>
            <div class="metric-box">
                <div class="metric-val">{collected['llm_calls']}</div>
                <div class="metric-lbl">Total LLM Inferences</div>
            </div>
            <div class="metric-box">
                <div class="metric-val">100%</div>
                <div class="metric-lbl">Success Rate</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Render Premium Final Travel Plan Panel
        if collected["final_response"]:
            st.markdown("<h3>🎯 Comprehensive Travel Dossier</h3>", unsafe_allow_html=True)
            st.markdown(f"<div class='final-card'>{collected['final_response']}</div>", unsafe_allow_html=True)

        # File Handling & Export Module
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"travel_plan_{timestamp}.md"
        save_dir = os.path.join(os.path.dirname(__file__), "travel_plans")
        os.makedirs(save_dir, exist_ok=True)

        file_content = f"""# Comprehensive Travel Dossier
**User Route Request:** {user_query}
**Created On:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**User Thread ID:** {thread_id}

---

## ✈️ Flight Analysis & Options
{collected['flight_results'] or 'N/A'}

---

## 🏨 Curated Stays & Hotels
{collected['hotel_results'] or 'N/A'}

---

## 🗓️ Detailed Route Map & Schedule
{collected['itinerary'] or 'N/A'}

---

## 🎯 Executive Synthesis Plan
{collected['final_response'] or 'N/A'}

---
*System Meta Metrics - LLM Inferences: {collected['llm_calls']}*
"""
        with open(os.path.join(save_dir, filename), "w", encoding="utf-8") as f:
            f.write(file_content)

        # Interactive Download Area
        dl_col, info_col = st.columns([1, 3])
        with dl_col:
            st.download_button("⬇️ Download Travel Pack", data=file_content,
                               file_name=filename, mime="text/markdown",
                               use_container_width=True)
        with info_col:
            st.markdown(f"""
            <div class='save-bar'>
                <span>📁 <b>Auto-Saved Securely:</b></span>
                <code>travel_plans/{filename}</code>
            </div>
            """, unsafe_allow_html=True)