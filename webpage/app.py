# BoE study website — run with:  streamlit run app.py
import streamlit as st

from data import UNITS, UNIT_TITLES, level_of

# ---- 1. Page settings (browser tab title and icon) ----
st.set_page_config(page_title="BoE Question Bank", page_icon="📘", layout="wide")

# ---- Look and feel: a little CSS to make the page bright and clean ----
st.markdown(
    """
    <style>
    .stApp { background: #f6f8fc; }
    [data-testid="stSidebar"] { background: #ffffff; border-right: 1px solid #e3e8f2; }
    .block-container { padding-top: 2rem; max-width: 1100px; }

    /* Blue banner at the top of the page */
    .hero {
        background: linear-gradient(120deg, #2563eb, #4f8df7);
        color: white; padding: 1.6rem 2rem; border-radius: 16px;
        margin-bottom: 1.2rem; box-shadow: 0 6px 20px rgba(37,99,235,0.18);
    }
    .hero .tag { font-size: 0.85rem; opacity: 0.85; letter-spacing: 0.05em; text-transform: uppercase; }
    .hero h1 { color: white; margin: 0.2rem 0 0.4rem; font-size: 1.9rem; }
    .hero p { margin: 0; opacity: 0.9; }

    /* Section headings (Apply / Analyze / Evaluate) */
    .level-head {
        margin: 1.6rem 0 0.6rem; padding-left: 0.7rem;
        border-left: 5px solid #2563eb; font-size: 1.2rem; font-weight: 700; color: #1e293b;
    }

    /* Each question becomes a white card */
    [data-testid="stExpander"] {
        background: #ffffff; border: 1px solid #e3e8f2 !important;
        border-radius: 12px !important; margin-bottom: 0.6rem;
        box-shadow: 0 1px 3px rgba(15,23,42,0.04);
    }
    [data-testid="stExpander"] summary p { font-weight: 600; color: #1e293b; }
    [data-testid="stExpander"]:hover { border-color: #93b4f5 !important; }

    /* Tables inside answers */
    table { border-collapse: collapse; width: 100%; }
    thead tr th { background: #eef3fe !important; color: #1e3a8a !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- 2. Sidebar: choose unit, level and search ----
st.sidebar.title("📘 BoE Question Bank")

unit = st.sidebar.radio("Choose a unit", list(UNITS.keys()))

level = st.sidebar.selectbox(
    "Bloom's level",
    ["All", "L3 – Apply", "L4 – Analyze", "L5 – Evaluate"],
)

search = st.sidebar.text_input("🔍 Search (e.g. MOSFET, sensor)")

show_all = st.sidebar.checkbox("Open all answers")

st.sidebar.markdown("---")
st.sidebar.caption("*[Outside notes]* = not from the class notes")
st.sidebar.caption("*(corrected)* = fixed a gap or mistake in the notes")

# ---- 3. Main heading ----
st.markdown(
    f"""
    <div class="hero">
        <div class="tag">Basics of Engineering · {unit}</div>
        <h1>{UNIT_TITLES[unit]}</h1>
        <p>30 questions · 5 marks each · Apply → Analyze → Evaluate</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---- 4. Pick which questions to show ----
# If something is typed in search, look through ALL units; otherwise only the chosen one.
if search:
    units_to_search = UNITS.keys()
else:
    units_to_search = [unit]

results = []
for u in units_to_search:
    for no, question, answer in UNITS[u]:
        if level != "All" and level_of(no) != level:
            continue
        text = (question + " " + answer).lower()
        if search and search.lower() not in text:
            continue
        results.append((u, no, question, answer))

if search:
    st.info(f'{len(results)} result(s) for "{search}" across all units')

if not results:
    st.warning("No questions match. Try a different word or level.")

# ---- 5. Show each question as a click-to-open box ----
current_level = None
for u, no, question, answer in results:
    # Print a heading when the Bloom's level changes (Apply → Analyze → Evaluate)
    if not search and level_of(no) != current_level:
        current_level = level_of(no)
        st.markdown(f'<div class="level-head">{current_level}</div>', unsafe_allow_html=True)

    label = f"Q{no}. {question}"
    if search:
        label = f"[{u}] " + label

    with st.expander(label, expanded=show_all or bool(search)):
        st.markdown(answer)
