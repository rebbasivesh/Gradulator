import tkinter as tk
from tkinter import messagebox

def SGPA_UI(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    frame = tk.Frame(parent)
    frame.pack()

    tk.Label(frame, text="SGPA Calculator", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

    credit_entries, grade_entries, labels = [], [], []

    def add_course():
        row = len(credit_entries) + 2
        label = tk.Label(frame, text=f"Course {row - 1}", width=10)
        credit = tk.Entry(frame, width=10)
        grade = tk.Entry(frame, width=10)
        label.grid(row=row, column=0, padx=5, pady=3)
        credit.grid(row=row, column=1, padx=5)
        grade.grid(row=row, column=2, padx=5)
        labels.append(label)
        credit_entries.append(credit)
        grade_entries.append(grade)

    def remove_course():
        if credit_entries:
            labels[-1].destroy()
            credit_entries[-1].destroy()
            grade_entries[-1].destroy()
            labels.pop(), credit_entries.pop(), grade_entries.pop()

    def reset():
        for w in credit_entries + grade_entries + labels:
            w.destroy()
        credit_entries.clear(), grade_entries.clear(), labels.clear()
        for _ in range(5):
            add_course()
        result_label.config(text="")

    def calculate_sgpa():
        try:
            total_credits, total_points = 0, 0
            for c, g in zip(credit_entries, grade_entries):
                credit = float(c.get())
                grade = float(g.get())
                if not 0 <= grade <= 10:
                    raise ValueError
                total_credits += credit
                total_points += credit * grade
            sgpa = total_points / total_credits
            result_label.config(text=f"SGPA: {sgpa:.2f} (Credits: {total_credits})", fg="blue")
        except:
            messagebox.showerror("Error", "Invalid inputs. Grade point should be 0–10.")

    def go_back():
        from main import show_main_menu
        show_main_menu()

    # Headings
    tk.Label(frame, text="Course").grid(row=1, column=0)
    tk.Label(frame, text="Credits").grid(row=1, column=1)
    tk.Label(frame, text="Grade Point").grid(row=1, column=2)

    for _ in range(5):
        add_course()

    tk.Button(frame, text="Add Course", command=add_course, bg="orange").grid(row=100, column=0, pady=10)
    tk.Button(frame, text="Remove Course", command=remove_course, bg="red", fg="white").grid(row=100, column=1)
    tk.Button(frame, text="Reset", command=reset, bg="gray", fg="white").grid(row=100, column=2)
    tk.Button(frame, text="Calculate SGPA", command=calculate_sgpa, bg="green", fg="white", width=30).grid(row=101, column=0, columnspan=3, pady=10)
    tk.Button(frame, text="⬅ Back", command=go_back, bg="lightblue").grid(row=102, column=0, columnspan=3, pady=5)

    result_label = tk.Label(frame, text="", font=("Arial", 12))
    result_label.grid(row=103, column=0, columnspan=3)

def CGPA_UI(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    frame = tk.Frame(parent)
    frame.pack()

    tk.Label(frame, text="CGPA Calculator", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

    sgpa_entries, credit_entries, labels = [], [], []

    def add_sem():
        row = len(sgpa_entries) + 2
        label = tk.Label(frame, text=f"Sem {row - 1}", width=10)
        sgpa = tk.Entry(frame, width=10)
        credit = tk.Entry(frame, width=10)
        label.grid(row=row, column=0, padx=5, pady=3)
        sgpa.grid(row=row, column=1, padx=5)
        credit.grid(row=row, column=2, padx=5)
        labels.append(label)
        sgpa_entries.append(sgpa)
        credit_entries.append(credit)

    def remove_sem():
        if sgpa_entries:
            labels[-1].destroy()
            sgpa_entries[-1].destroy()
            credit_entries[-1].destroy()
            labels.pop(), sgpa_entries.pop(), credit_entries.pop()

    def reset():
        for w in sgpa_entries + credit_entries + labels:
            w.destroy()
        sgpa_entries.clear(), credit_entries.clear(), labels.clear()
        for _ in range(2):
            add_sem()
        result_label.config(text="")

    def calculate_cgpa():
        try:
            total_credits, total_points = 0, 0
            for s, c in zip(sgpa_entries, credit_entries):
                sgpa = float(s.get())
                credit = float(c.get())
                total_credits += credit
                total_points += sgpa * credit
            cgpa = total_points / total_credits
            result_label.config(text=f"CGPA: {cgpa:.2f} (Credits: {total_credits})", fg="green")
        except:
            messagebox.showerror("Error", "Invalid SGPA or Credit inputs.")

    def go_back():
        from main import show_main_menu
        show_main_menu()

    # Headings
    tk.Label(frame, text="Semester").grid(row=1, column=0)
    tk.Label(frame, text="SGPA").grid(row=1, column=1)
    tk.Label(frame, text="Credits").grid(row=1, column=2)

    for _ in range(2):
        add_sem()

    tk.Button(frame, text="Add Semester", command=add_sem, bg="orange").grid(row=100, column=0, pady=10)
    tk.Button(frame, text="Remove Semester", command=remove_sem, bg="red", fg="white").grid(row=100, column=1)
    tk.Button(frame, text="Reset", command=reset, bg="gray", fg="white").grid(row=100, column=2)
    tk.Button(frame, text="Calculate CGPA", command=calculate_cgpa, bg="blue", fg="white", width=30).grid(row=101, column=0, columnspan=3, pady=10)
    tk.Button(frame, text="⬅ Back", command=go_back, bg="lightblue").grid(row=102, column=0, columnspan=3, pady=5)

    result_label = tk.Label(frame, text="", font=("Arial", 12))
    result_label.grid(row=103, column=0, columnspan=3)
