import streamlit as st

st.set_page_config(page_title="KLU SGPA & CGPA Calculator", layout="centered")

# --- MAIN MENU ---
if "page" not in st.session_state:
    st.session_state.page = "menu"

def show_main_menu():
    st.session_state.page = "menu"

def go_to_sgpa():
    st.session_state.page = "sgpa"

def go_to_cgpa():
    st.session_state.page = "cgpa"

# --- MENU SCREEN ---
if st.session_state.page == "menu":
    st.title("📘 What do you want to calculate?")
    st.markdown("")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("✅ SGPA Calculator", on_click=go_to_sgpa, use_container_width=True)
        st.button("📊 CGPA Calculator", on_click=go_to_cgpa, use_container_width=True)

# --- SGPA CALCULATOR ---
elif st.session_state.page == "sgpa":
    st.title("🎓 SGPA Calculator")

    if "sgpa_count" not in st.session_state:
        st.session_state.sgpa_count = 5

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Add Course"):
            st.session_state.sgpa_count += 1
    with col2:
        if st.button("➖ Remove Course") and st.session_state.sgpa_count > 1:
            st.session_state.sgpa_count -= 1
    with col3:
        if st.button("🔄 Reset"):
            st.session_state.sgpa_count = 5

    st.markdown("### Enter Course Details")
    credits = []
    grades = []

    for i in range(st.session_state.sgpa_count):
        col1, col2, col3 = st.columns([1, 2, 2])
        with col1:
            st.markdown(f"**Course {i+1}**")
        with col2:
            c = st.number_input(f"Credits {i+1}", key=f"sc{i}", step=0.5, min_value=0.0)
        with col3:
            g = st.number_input(f"Grade Point {i+1}", key=f"sg{i}", step=0.1, min_value=0.0, max_value=10.0)
        credits.append(c)
        grades.append(g)

    if st.button("✅ Calculate SGPA"):
        try:
            total_c = sum(credits)
            total_gp = sum(c * g for c, g in zip(credits, grades))
            if total_c == 0:
                raise ValueError
            sgpa = total_gp / total_c
            st.success(f"🎯 SGPA: {sgpa:.2f} (Total Credits: {total_c})")
        except:
            st.error("⚠️ Invalid input!")

    st.button("⬅ Back to Menu", on_click=show_main_menu)

# --- CGPA CALCULATOR ---
elif st.session_state.page == "cgpa":
    st.title("🏆 CGPA Calculator")

    if "cgpa_count" not in st.session_state:
        st.session_state.cgpa_count = 2

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Add Semester"):
            st.session_state.cgpa_count += 1
    with col2:
        if st.button("➖ Remove Semester") and st.session_state.cgpa_count > 1:
            st.session_state.cgpa_count -= 1
    with col3:
        if st.button("🔄 Reset"):
            st.session_state.cgpa_count = 2

    st.markdown("### Enter Semester SGPA and Credits")
    sgpas = []
    credits = []

    for i in range(st.session_state.cgpa_count):
        col1, col2, col3 = st.columns([1, 2, 2])
        with col1:
            st.markdown(f"**Semester {i+1}**")
        with col2:
            s = st.number_input(f"SGPA {i+1}", key=f"cgpa{i}", min_value=0.0, max_value=10.0, step=0.1)
        with col3:
            c = st.number_input(f"Credits {i+1}", key=f"cgcred{i}", min_value=0.0, step=0.5)
        sgpas.append(s)
        credits.append(c)

    if st.button("📊 Calculate CGPA"):
        try:
            total_c = sum(credits)
            total_sgpa = sum(s * c for s, c in zip(sgpas, credits))
            if total_c == 0:
                raise ValueError
            cgpa = total_sgpa / total_c
            st.success(f"🏆 CGPA: {cgpa:.2f} (Total Credits: {total_c})")
        except:
            st.error("⚠️ Invalid input!")

    st.button("⬅ Back to Menu", on_click=show_main_menu)
