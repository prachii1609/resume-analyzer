import streamlit as st
import re
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from ats_score import calculate_ats_score

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.markdown("Upload your resume and get instant analysis 🚀")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    cleaned = clean_text(text)

    skills = extract_skills(cleaned)
    score = calculate_ats_score(skills)

    st.subheader("✅ Skills Found")
    st.write(skills)

    st.subheader("📊 ATS Score")
    st.progress(score)
    st.write(f"{score}/100")

    st.subheader("💡 Suggestions")

    required_skills = [
        "python", "machine learning", "sql",
        "data science", "pandas", "deep learning"
    ]

    for skill in required_skills:
        if skill not in skills:
            st.warning(f"Add {skill}")

    if all(skill in skills for skill in required_skills):
        st.success("Great! Your resume looks strong 💪")
