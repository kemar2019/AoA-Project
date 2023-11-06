
from parser import parse_chat_log
from analyzer import analyze_responses
from grader import assign_grades

import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

# Assuming the other modules (parse_chat_log, analyze_responses, assign_grades) have been defined as before

def load_chat_log():
    # Open a file dialog to select the chat log
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            chat_log_content = file.read()

        tutor_questions, participants = parse_chat_log(chat_log_content)
        scores = analyze_responses(tutor_questions, participants)
        grades = assign_grades(scores)

        # Display the grades in the text area
        grades_display.delete(1.0, tk.END)  # Clear the text area
        for participant, grade in grades.items():
            grades_display.insert(tk.END, f"{participant}: {grade}\n")

# Set up the main application window
root = tk.Tk()
root.title("Chat Grader")

# Add a button to load the chat log
load_button = tk.Button(root, text="Load Chat Log", command=load_chat_log)
load_button.pack()

# Add a scrolled text area to display the grades
grades_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
grades_display.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
