skills_list = [
    "python", "java", "c++", "machine learning",
    "data science", "sql", "excel", "deep learning",
    "nlp", "tensorflow", "pandas", "html", "css"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []
    
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    
    return found_skills
