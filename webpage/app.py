# BoE study website — run with:  streamlit run app.py
import streamlit as st

from data import UNITS, UNIT_TITLES, level_of

# ---- 1. Page settings (browser tab title and icon) ----
st.set_page_config(page_title="BoE Question Bank", page_icon="📘", layout="wide")

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
st.title(f"{unit}: {UNIT_TITLES[unit]}")
st.caption("30 questions · 5 marks each")

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
        st.subheader(current_level)

    label = f"Q{no}. {question}"
    if search:
        label = f"[{u}] " + label

    with st.expander(label, expanded=show_all or bool(search)):
        st.markdown(answer)
