# BoE study website — run with:  streamlit run app.py
import json
from pathlib import Path

import pypdfium2 as pdfium
import streamlit as st

from data import UNITS, UNIT_TITLES, level_of
from revision import REVISION

HERE = Path(__file__).parent
MATERIALS = HERE / "materials"
GITHUB_RAW = "https://github.com/rpeyyety-luffy/semester1/raw/main/webpage/materials/"

# Which PDF file holds the notes and the slides for each unit
FILES = {
    "Unit 1": {"Notes": "unit1_notes.pdf", "Slides": "unit1_slides.pdf"},
    "Unit 2": {"Notes": "unit2_notes.pdf", "Slides": "unit2_slides.pdf"},
    "Unit 3": {"Notes": "unit3_notes.pdf", "Slides": "unit3_slides.pdf"},
}

# ---- 1. Page settings ----
st.set_page_config(page_title="BoE Study Hub", page_icon="📘", layout="wide")

# ---- 2. Look and feel: CSS for a bright, clean page ----
st.markdown(
    """
    <style>
    .stApp { background: #f6f8fc; }
    [data-testid="stSidebar"] { background: #ffffff; border-right: 1px solid #e3e8f2; }
    .block-container { padding-top: 2rem; max-width: 1100px; }

    .hero {
        background: linear-gradient(120deg, #2563eb, #4f8df7);
        color: white; padding: 1.6rem 2rem; border-radius: 16px;
        margin-bottom: 1rem; box-shadow: 0 6px 20px rgba(37,99,235,0.18);
    }
    .hero .tag { font-size: 0.85rem; opacity: 0.85; letter-spacing: 0.05em; text-transform: uppercase; }
    .hero h1 { color: white; margin: 0.2rem 0 0.4rem; font-size: 1.9rem; }
    .hero p { margin: 0; opacity: 0.9; }

    .level-head {
        margin: 1.4rem 0 0.6rem; padding-left: 0.7rem;
        border-left: 5px solid #2563eb; font-size: 1.2rem; font-weight: 700; color: #1e293b;
    }

    [data-testid="stExpander"] {
        background: #ffffff; border: 1px solid #e3e8f2 !important;
        border-radius: 12px !important; margin-bottom: 0.6rem;
        box-shadow: 0 1px 3px rgba(15,23,42,0.04);
    }
    [data-testid="stExpander"] summary p { font-weight: 600; color: #1e293b; }
    [data-testid="stExpander"]:hover { border-color: #93b4f5 !important; }

    [data-testid="stButtonGroup"] button { font-weight: 600; padding: 0.45rem 1.1rem; }

    table { border-collapse: collapse; width: 100%; }
    thead tr th { background: #eef3fe !important; color: #1e3a8a !important; }
    .page-img img { border-radius: 10px; border: 1px solid #e3e8f2; box-shadow: 0 2px 10px rgba(15,23,42,0.06); }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---- 3. Helper functions for the PDF pages (cached so they're only done once) ----
@st.cache_data
def load_index():
    """Text of every PDF page, made beforehand, used for search."""
    return json.loads((MATERIALS / "search_index.json").read_text())


@st.cache_data
def page_count(filename):
    return len(pdfium.PdfDocument(str(MATERIALS / filename)))


@st.cache_data(max_entries=20)
def page_image(filename, page_no):
    """Turn one PDF page (1-based) into a picture."""
    pdf = pdfium.PdfDocument(str(MATERIALS / filename))
    return pdf[page_no - 1].render(scale=1.3).to_pil()


def show_page(filename, page_no):
    st.markdown('<div class="page-img">', unsafe_allow_html=True)
    st.image(page_image(filename, page_no), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


def pdf_viewer(unit, kind):
    """Page-by-page viewer with Prev / Next buttons and a download button."""
    filename = FILES[unit][kind]
    total = page_count(filename)
    key = f"{unit}-{kind}-page"
    if key not in st.session_state:
        st.session_state[key] = 1

    def move(step):
        st.session_state[key] = min(max(1, st.session_state[key] + step), total)

    c1, c2, c3, c4 = st.columns([1, 2, 1, 2])
    c1.button("◀ Prev", key=key + "-prev", on_click=move, args=(-1,), use_container_width=True)
    c2.number_input("Page", 1, total, key=key, label_visibility="collapsed")
    c3.button("Next ▶", key=key + "-next", on_click=move, args=(1,), use_container_width=True)
    # Download straight from GitHub so the app doesn't have to send big files itself
    c4.link_button(f"⬇ Download {kind} PDF", GITHUB_RAW + filename, use_container_width=True)
    st.caption(f"Page {st.session_state[key]} of {total}")
    show_page(filename, st.session_state[key])


def show_questions(rows, open_all, searching):
    current_level = None
    for u, no, question, answer in rows:
        if not searching and level_of(no) != current_level:
            current_level = level_of(no)
            st.markdown(f'<div class="level-head">{current_level}</div>', unsafe_allow_html=True)
        label = f"Q{no}. {question}"
        if searching:
            label = f"[{u}] " + label
        with st.expander(label, expanded=open_all):
            st.markdown(answer)


# ---- 4. Sidebar ----
st.sidebar.title("📘 BoE Study Hub")
unit = st.sidebar.radio("Choose a unit", list(UNITS.keys()))
search = st.sidebar.text_input("🔍 Search everything", placeholder="e.g. MOSFET, forging, sensor")
st.sidebar.markdown("---")
st.sidebar.caption("**Q&A tags**")
st.sidebar.caption("*[Outside notes]* = not from the class notes")
st.sidebar.caption("*(corrected)* = fixed a gap or mistake in the notes")

# ---- 5. Heading ----
st.markdown(
    f"""
    <div class="hero">
        <div class="tag">Basics of Engineering · {unit}</div>
        <h1>{UNIT_TITLES[unit]}</h1>
        <p>Q&A · Study notes · Slides · Quick revision — all in one place</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---- 6a. Search mode: look through Q&A, notes and slides of ALL units ----
if search:
    word = search.lower()
    qa_hits = [
        (u, no, q, a)
        for u in UNITS
        for no, q, a in UNITS[u]
        if word in (q + " " + a).lower()
    ]
    index = load_index()
    page_hits = []
    for u, kinds in FILES.items():
        for kind, filename in kinds.items():
            for i, text in enumerate(index[filename]):
                pos = text.lower().find(word)
                if pos != -1:
                    snippet = text[max(0, pos - 90): pos + 140]
                    page_hits.append((u, kind, filename, i + 1, snippet))

    st.info(f'**"{search}"** — {len(qa_hits)} question(s) and {len(page_hits)} page(s) in notes / slides')

    if qa_hits:
        st.markdown('<div class="level-head">❓ Questions</div>', unsafe_allow_html=True)
        show_questions(qa_hits, open_all=False, searching=True)

    if page_hits:
        st.markdown('<div class="level-head">📄 Notes & slides pages</div>', unsafe_allow_html=True)
        for u, kind, filename, page_no, snippet in page_hits[:40]:
            with st.expander(f"[{u}] {kind} — page {page_no}:  …{snippet}…"):
                show_page(filename, page_no)
        if len(page_hits) > 40:
            st.caption(f"Showing the first 40 of {len(page_hits)} pages — try a more specific word.")

    if not qa_hits and not page_hits:
        st.warning("Nothing found. Try a different word. (Unit 2 notes are scanned images, so they can't be searched.)")

# ---- 6b. Normal mode: tabs for the chosen unit ----
else:
    # Only the chosen section is built (lighter and faster than tabs, which build all 4)
    section = st.segmented_control(
        "Section",
        ["❓ Q&A", "📝 Study notes", "📊 Slides", "⚡ Quick revision"],
        default="❓ Q&A",
        label_visibility="collapsed",
    ) or "❓ Q&A"

    if section == "❓ Q&A":
        col1, col2 = st.columns([2, 1])
        level = col1.selectbox(
            "Bloom's level", ["All", "L3 – Apply", "L4 – Analyze", "L5 – Evaluate"]
        )
        col2.write("")
        open_all = col2.checkbox("Open all answers")
        rows = [
            (unit, no, q, a)
            for no, q, a in UNITS[unit]
            if level == "All" or level_of(no) == level
        ]
        show_questions(rows, open_all, searching=False)

    elif section == "📝 Study notes":
        pdf_viewer(unit, "Notes")

    elif section == "📊 Slides":
        pdf_viewer(unit, "Slides")

    else:
        st.markdown(REVISION[unit])
