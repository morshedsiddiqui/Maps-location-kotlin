import tkinter as tk
from tkinter import ttk, messagebox

class GUIApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI Application")
        self.geometry("400x300")
        
        # Initialize variables for widgets
        self.full_name_var = tk.StringVar()
        self.residency_var = tk.StringVar()
        self.program_var = tk.StringVar()
        self.courses_var = [tk.StringVar() for _ in range(3)]
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame
        frame = ttk.Frame(self, padding="10", relief="sunken")
        frame.grid(row=0, column=0, sticky="nsew")

        # Label for the data-entry form
        ttk.Label(frame, text="Data Entry Form", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Labels and Entry widgets
        ttk.Label(frame, text="Full name:").grid(row=1, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.full_name_var).grid(row=1, column=1)

        ttk.Label(frame, text="Residency:").grid(row=2, column=0, sticky="e")
        ttk.Radiobutton(frame, text="Domestic", variable=self.residency_var, value="dom").grid(row=2, column=1, sticky="w")
        ttk.Radiobutton(frame, text="International", variable=self.residency_var, value="intl").grid(row=3, column=1, sticky="w")

        ttk.Label(frame, text="Program:").grid(row=4, column=0, sticky="e")
        ttk.Combobox(frame, textvariable=self.program_var, values=["AI", "Gaming", "Health", "Software"]).grid(row=4, column=1)

        ttk.Label(frame, text="Courses:").grid(row=5, column=0, sticky="e")
        ttk.Checkbutton(frame, text="Programming I", variable=self.courses_var[0], onvalue="COMP100", offvalue="").grid(row=5, column=1, sticky="w")
        ttk.Checkbutton(frame, text="Web Page Design", variable=self.courses_var[1], onvalue="COMP213", offvalue="").grid(row=6, column=1, sticky="w")
        ttk.Checkbutton(frame, text="Software Engineering", variable=self.courses_var[2], onvalue="COMP120", offvalue="").grid(row=7, column=1, sticky="w")

        # Buttons
        ttk.Button(frame, text="Reset", command=self.reset_form).grid(row=8, column=0, pady=(10, 0))
        ttk.Button(frame, text="Ok", command=self.show_message).grid(row=8, column=1, pady=(10, 0))
        ttk.Button(frame, text="Exit", command=self.destroy).grid(row=9, column=0, columnspan=2, pady=(10, 0))

        # Resize configuration
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(8, weight=1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def reset_form(self):
        # Reset all widget values
        self.full_name_var.set("")
        self.residency_var.set("")
        self.program_var.set("")
        for course_var in self.courses_var:
            course_var.set("")

    def show_message(self):
        # Show messagebox with form information
        message = (
            f"Full name: {self.full_name_var.get()}\n"
            f"Residency: {self.residency_var.get()}\n"
            f"Program: {self.program_var.get()}\n"
            f"Courses: {', '.join([course.get() for course in self.courses_var if course.get()])}"
        )
        messagebox.showinfo("Form Information", message)

# Main
if __name__ == "__main__":
    app = GUIApplication()
    app.mainloop()

