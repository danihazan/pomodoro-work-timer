import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
work_count=0
timer= None
def main():
    # ---------------------------- TIMER RESET ------------------------------- #

    def reset_timer():
        global reps,work_count,timer
        if timer is not None:
            window.after_cancel(timer)
        canvas.itemconfig(timer_text,text="00:00")
        head_label.config(text="Timer",fg=GREEN)
        check_marks.config(text="")
        reps=0
        work_count=0
        timer=None

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start_timer():
        global reps
        global work_count
        reps += 1
        if reps % 2 !=0:
            work_count += 1
            head_label.config(text="Work",fg=GREEN)
            count_down(WORK_MIN * 60)
        elif reps % 8 ==0:
            head_label.config(text="Break",fg=RED)
            count_down(LONG_BREAK_MIN * 60)

        else:
            head_label.config(text="Break",fg=PINK)
            count_down(SHORT_BREAK_MIN * 60)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def count_down(count):
        global timer
        minutes= math.floor(count/60)
        seconds=count%60
        canvas.itemconfig(timer_text,text=f"{minutes:02d}:{seconds:02d}")
        if count > 0:
            timer=window.after(1000, count_down, count - 1)
        else:
            checks_text="✔"*work_count
            check_marks.config(text=checks_text, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 8, "bold"))
            start_timer()

    # ---------------------------- UI SETUP ------------------------------- #

    window=tk.Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50,bg=YELLOW)

    canvas=tk.Canvas(width=220,height=224,bg=YELLOW,highlightthickness=0)
    tomato_img= tk.PhotoImage(file="tomato.png")
    canvas.create_image(102,112,image=tomato_img)
    timer_text=canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
    canvas.grid(column=1,row=1)

    #Header
    head_label = tk.Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
    head_label.grid(column=1,row=0)

    #check_marks
    check_marks=tk.Label(text="",bg=YELLOW,fg=GREEN,font=(FONT_NAME,8,"bold"))
    check_marks.grid(column=1,row=3)


    #Start Button
    start_button=tk.Button(text="Start",font=(FONT_NAME,10,"bold"),highlightthickness=0,command=start_timer)
    start_button.grid(column=0,row=2)

    #Reset Button
    reset_button=tk.Button(text="Reset",font=(FONT_NAME,10,"bold"),highlightthickness=0,command=reset_timer)
    reset_button.grid(column=2,row=2)


    window.mainloop()

if __name__ == "__main__":
    main()