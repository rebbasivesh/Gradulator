import streamlit as st

st.set_page_config(page_title="KLU SGPA & CGPA Calculator", layout="centered")
st.title("🎓 KLU SGPA Calculator")

num_courses = st.number_input("How many courses do you have?", min_value=1, max_value=20, value=5)

credits = []
grades = []

st.write("### Enter Credits and Grade Points:")
for i in range(num_courses):
    col1, col2 = st.columns(2)
    with col1:
        credit = st.number_input(f"Course {i+1} - Credits", key=f"credit{i}")
    with col2:
        grade = st.number_input(f"Course {i+1} - Grade Point", key=f"grade{i}", min_value=0.0, max_value=10.0, step=0.1)
    credits.append(credit)
    grades.append(grade)

if st.button("🧮 Calculate SGPA"):
    try:
        total_credits = sum(credits)
        total_points = sum(c * g for c, g in zip(credits, grades))
        sgpa = total_points / total_credits
        st.success(f"✅ SGPA: {sgpa:.2f} (Total Credits: {total_credits})")
    except:
        st.error("⚠️ Please make sure all fields are filled correctly.")
