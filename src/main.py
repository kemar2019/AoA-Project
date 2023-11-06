
from parser import parse_chat_log
from analyzer import analyze_responses
from grader import assign_grades
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

def load_chat_log():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            chat_log_content = file.read()

        tutor_questions, participants = parse_chat_log(chat_log_content)
        scores, questions_answered, participation_levels = analyze_responses(tutor_questions, participants)
        grades = assign_grades(scores)

        # Update the display
        display.delete('1.0', tk.END)
        display.insert(tk.END, 'Tutor Questions:\n')
        for question in tutor_questions:
            display.insert(tk.END, f'{question}\n')
        display.insert(tk.END, '\nStudent Grades and Participation:\n')
        for name in sorted(participants):
            display.insert(tk.END, f'{name}: Grade {grades[name]}, Score {scores[name]}, Questions Answered {questions_answered[name]}, Participation Level {participation_levels[name]}\n')

root = tk.Tk()
root.title('Chat Grader')

display = scrolledtext.ScrolledText(root, height=30)
display.pack()

load_button = tk.Button(root, text='Load Chat Log', command=load_chat_log)
load_button.pack()

root.mainloop()
