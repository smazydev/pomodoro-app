from tkinter import *


#------------ CONSTANTS ---------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ------- UI SETUP --------- #
window = Tk()
window.title("Pomodoro GUI Application")
window.minsize(width=400,height=150)
window.configure(bg="black")

time_label = Label(text="00:00", fg="white",bg="black",font=(FONT_NAME,50))
time_label.pack()

start_button = Button(text="start",width=10,bg=GREEN,fg="white")
start_button.pack()
reset_button = Button(text="reset",width=10,bg=RED,fg="white")
reset_button.pack()

window.mainloop()
