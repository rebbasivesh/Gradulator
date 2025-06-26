import tkinter as tk
from ui import SGPA_UI, CGPA_UI

def show_main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    choice_frame = tk.Frame(root)
    choice_frame.pack(pady=40)

    tk.Label(choice_frame, text="What do you want to calculate?", font=("Arial", 14, "bold")).pack(pady=10)

    content_frame = tk.Frame(root)

    def show_sgpa():
        choice_frame.pack_forget()
        SGPA_UI(root)

    def show_cgpa():
        choice_frame.pack_forget()
        CGPA_UI(root)

    tk.Button(choice_frame, text="SGPA Calculator", width=20, command=show_sgpa, bg="green", fg="white").pack(pady=5)
    tk.Button(choice_frame, text="CGPA Calculator", width=20, command=show_cgpa, bg="blue", fg="white").pack(pady=5)

root = tk.Tk()
root.title("KLU Grade Point Calculator")
root.geometry("500x600")

show_main_menu()
root.mainloop()
