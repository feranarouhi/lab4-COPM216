import tkinter
from tkinter import ttk
from tkinter import messagebox

def reset_form():
    fullname_entry.delete(0, 'end')
    program_combobox.set('')
    checkvar1.set(False)
    checkvar2.set(False)
    checkvar3.set(False)
    residency_var.set("Domestic")

def show_message():
    fullname = fullname_entry.get()
    program = program_combobox.get()
    courses = []
    if checkvar1.get():
        courses.append("Programming I")
    if checkvar2.get():
        courses.append("Software Engineering")
    if checkvar3.get():
        courses.append("Web Page Design")
    residency = residency_var.get()

    message = f"Fullname: {fullname}\nProgram: {program}\nCourses: {', '.join(courses)}\nResidency: {residency}"

    messagebox.showinfo("Form Information", message)

def on_checkbox_toggle():
    # Add logic to update selected courses
    pass

def on_radiobutton_toggle():
    # Add logic to update residency status
    pass

window = tkinter.Tk()
window.title('Centennial College')
window.geometry('600x400')

frame = tkinter.Frame(window)
frame.pack(fill='both', expand=True)

topic_label = tkinter.Label(frame, text="ICET Student Survey", font=("Arial", 20))

# Create widgets
fullname_label = tkinter.Label(frame, text="Fullname:")
fullname_entry = tkinter.Entry(frame)

program_label = tkinter.Label(frame, text="Program:")
program_combobox = ttk.Combobox(frame, values=["AI", "Gaming", "Health", "Softwares"])

courses_label = tkinter.Label(frame, text="Courses:")

# CheckVar for courses
checkvar1 = tkinter.BooleanVar()
checkvar2 = tkinter.BooleanVar()
checkvar3 = tkinter.BooleanVar()

course_checkbox1 = tkinter.Checkbutton(frame, text="Programming I", variable=checkvar1, command=on_checkbox_toggle)
course_checkbox2 = tkinter.Checkbutton(frame, text="Software Engineering", variable=checkvar2, command=on_checkbox_toggle)
course_checkbox3 = tkinter.Checkbutton(frame, text="Web Page Design", variable=checkvar3, command=on_checkbox_toggle)

# Radiobuttons for residency
residency_label = tkinter.Label(frame, text="Residency:")

residency_var = tkinter.StringVar()
residency_var.set("Domestic")  # Default value

residency_radio1 = tkinter.Radiobutton(frame, text="Domestic", variable=residency_var, value="Domestic", command=on_radiobutton_toggle)
residency_radio2 = tkinter.Radiobutton(frame, text="International", variable=residency_var, value="International", command=on_radiobutton_toggle)

# Buttons
reset_button = tkinter.Button(frame, text="Reset", command=reset_form)
ok_button = tkinter.Button(frame, text="Ok", command=show_message)
exit_button = tkinter.Button(frame, text="Exit", command=window.quit)

# Display widgets
topic_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)

fullname_label.grid(row=1, column=0, padx=40, sticky='e')
fullname_entry.grid(row=1, column=1, pady=20, sticky='w')

program_label.grid(row=2, column=0, sticky='e')
program_combobox.grid(row=2, column=1, sticky='w')

courses_label.grid(row=3, column=0, sticky='e')

course_checkbox1.grid(row=3, column=1, sticky='w')
course_checkbox2.grid(row=4, column=1, sticky='w')
course_checkbox3.grid(row=5, column=1, sticky='w')

residency_label.grid(row=6, column=0, sticky='e')

residency_radio1.grid(row=6, column=1, sticky='w')
residency_radio2.grid(row=7, column=1, sticky='w')

reset_button.grid(row=8, column=0, pady=10)
ok_button.grid(row=8, column=1, pady=10)
exit_button.grid(row=8, column=2, pady=10)

for widget in frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()
