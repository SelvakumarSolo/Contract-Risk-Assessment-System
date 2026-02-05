import streamlit as st

# ===== Page config MUST be first =====
st.set_page_config(
    page_title="Contract Risk Assessment System",
    layout="wide"
)

from pathlib import Path

def load_css():
    css_path = Path(__file__).parent / "assets" / "ui.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


# ===== Backend imports =====
from backend.file_loader import load_file
from backend.preprocessor import clean_text
from backend.clause_splitter import split_clauses
from backend.risk_rules import detect_risk
from backend.risk_scorer import calculate_contract_risk
from backend.templates import suggest_alternative

# ===== Header =====
st.markdown("""
<div style="text-align:center; margin-bottom:40px;">
    <h1>Contract Risk Assessment System</h1>
    <p style="color:#d1d5db; font-size:16px;">
        AI-assisted legal document analysis and risk evaluation
    </p>
</div>
""", unsafe_allow_html=True)

# ===== File uploader =====
uploaded_file = st.file_uploader(
    "📤 Upload Contract Document (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

# ===== Main logic =====
if uploaded_file:
    raw_text = load_file(uploaded_file)
    cleaned_text = clean_text(raw_text)
    clauses = split_clauses(cleaned_text)

    risks = []

    st.markdown("### 📑 Clause-wise Risk Analysis")

    for clause in clauses:
        risk = detect_risk(clause)
        risks.append(risk)

        color = "🔴" if risk == "High" else "🟡" if risk == "Medium" else "🟢"

        with st.expander(f"{color} {risk} Risk Clause"):
            st.write(clause)
            st.info(suggest_alternative(risk))

    # ===== Final Risk Summary =====
    final_risk = calculate_contract_risk(risks)

    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.96);
        padding: 32px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 14px 35px rgba(0,0,0,0.3);
        margin-top: 40px;
    ">
        <h2 style="color:#111827;">Overall Contract Risk Level</h2>
        <h1 style="color:#dc2626;">{final_risk}</h1>
    </div>
    """, unsafe_allow_html=True)

