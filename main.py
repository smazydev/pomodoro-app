from tkinter import *
import math

#------------ CONSTANTS ---------------- #
RED = "#e7305b"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
#-------- TIMER ------- #
def start_timer():
    count_down(5 * 60)






#--------- COUNTDOWN -------- #
def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    time_label.config(text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,count_down,count-1)

# ------- UI SETUP --------- #
window = Tk()
window.title("Pomodoro GUI Application")
window.minsize(width=400,height=150)
window.configure(bg="black")
time_label = Label(text="00:00", fg="white",bg="black",font=(FONT_NAME,50))
time_label.pack()
start_button = Button(text="start",width=10,bg=GREEN,fg="white",command=start_timer)
start_button.pack()
reset_button = Button(text="reset",width=10,bg=RED,fg="white")
reset_button.pack()

window.mainloop()
