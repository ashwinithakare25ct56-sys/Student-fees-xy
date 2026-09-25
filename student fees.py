import tkinter as tk
from tkinter import messagebox

students = []

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    fees = fees_entry.get()
    
    if name == "" or roll == "" or fees == "":
        messagebox.showwarning("Warning", "Please fill all details")
        return

    students.append({
        "Roll No": roll,
        "Name": name,
        "Fees": fees
    })

    messagebox.showinfo("Success", "Student fees added successfully")

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    fees_entry.delete(0, tk.END)


def show_students():
    result = ""

    if len(students) == 0:
        result = "No student records found."
    else:
        for s in students:
            result += "Roll No: " + s["Roll No"] + "\n"
            result += "Name: " + s["Name"] + "\n"
            result += "Fees: ₹" + s["Fees"] + "\n"
            result += "----------------------\n"

    messagebox.showinfo("Student Records", result)


# Main Window
window = tk.Tk()
window.title("Student Fees Management System")
window.geometry("400x400")

title = tk.Label(
    window,
    text="Student Fees Management System",
    font=("Arial", 16, "bold")
)
title.pack(pady=20)

tk.Label(window, text="Roll No").pack()
roll_entry = tk.Entry(window)
roll_entry.pack(pady=5)

tk.Label(window, text="Student Name").pack()
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

tk.Label(window, text="Fees Amount").pack()
fees_entry = tk.Entry(window)
fees_entry.pack(pady=5)

tk.Button(
    window,
    text="Add Student",
    command=add_student
).pack(pady=15)

tk.Button(
    window,
    text="Show Students",
    command=show_students
).pack(pady=5)

tk.Button(
    window,
    text="Exit",
    command=window.destroy
).pack(pady=15)

window.mainloop()