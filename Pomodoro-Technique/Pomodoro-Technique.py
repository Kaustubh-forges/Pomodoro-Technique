#------------------------- POMODORO TECHNIQUE PROJECT-------------------------

#------------------------- MODULES IMPORTED-----------------------------------
from tkinter import * # Imports everything from "tkinter" module
import winsound # Produces sound effect
import time # Shows time for countdown
import math

# ---------------------------- CONSTANTS ------------------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS=0
CHECK_MARK="✔️"
timer=None

#--------------------------- TIMER RESET------------------------------------
def reset_timer():
    screen.after_cancel(timer)
    Timer.configure(text="Timer",font=("Ariel",24,"bold"),background=GREEN,fg="black")
    canvas.itemconfigure(canvas_text,text="00:00") # Updates canvas to display "00:00" after reset button is hit
    Check_mark.configure(text="") # Removes evidence of any previous countdowns
    global REPS
    REPS=0

# ---------------------------- TIMER MECHANISM -------------------------------
def start_clicked():
    global REPS
    REPS+=1
    # Tracks number of rounds to determine when work time, short break, or long break is conducted
    if REPS==1 or REPS==3 or REPS==5 or REPS==7:
        Timer.configure(text="Work Time",foreground="black")
        minutes = WORK_MIN
        seconds = 0
        count_down(seconds, minutes)

    elif REPS==2 or REPS==4 or REPS==6:
        Timer.configure(text="Short Break",foreground=RED)
        minutes=SHORT_BREAK_MIN
        seconds=0
        count_down(seconds,minutes)

    if REPS==8:
        Timer.configure(text="Long Break",foreground=PINK)
        minutes=LONG_BREAK_MIN
        seconds=0
        count_down(seconds,minutes)
        REPS=0
#---------Displaying Checkmarks according to reps--------
    sessions_done=math.floor(REPS / 2) # Gives the number of rounds made(one round means one work and break session each)
    Check_mark.configure(text=CHECK_MARK*sessions_done) # Displays checkmarks to relay the number of rounds completed
'''
Now, the way tkinter is working here, it basically adds REPS to 2 and simultaneously runs the check_mark configuration.
It runs both at the start of first short break(overall second rep), that is why we see the checkmark as soon as the second rep begins.
I was originally expecting it to add a checkmark after a short break round was over(which was not what I wanted), so imagine my surprise when this worked.
This gives the illusion that a checkmark is being added after a work session ends(which is what I wanted) even though it is added when a short break begins.
'''
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count_of_seconds,count_of_minutes):
    if count_of_minutes>=0:
        # Base case for handling the 00:00
        if count_of_minutes == 0 and count_of_seconds == 0:
            canvas.itemconfigure(canvas_text, text="0"+str(count_of_minutes) + ":" + str(
                count_of_seconds)+"0") # Displays "00:00"
            # Produces sound effect after a fixed amount of time
            for i in range(3):
                winsound.Beep(1000,300)
                time.sleep(0.1)
            return  # Ensures that the function terminates, and we can comfortably move from work time to break time by clicking "start" when needed.

        # To change an element of  the canvas.
        # We are accessing the canvas_text part in the canvas and then changing the text part of it.

        if count_of_seconds == 0:
            count_of_seconds = 59
            count_of_minutes -= 1
        # Conditional statements to uphold the "00::00" format
        if count_of_seconds<10:
            if count_of_minutes<10:
                canvas.itemconfigure(canvas_text, text=("0"+str(count_of_minutes) + ":" + "0" + str(
                count_of_seconds)))
            else:
                canvas.itemconfigure(canvas_text, text=(str(count_of_minutes) + ":" + "0"+ str(
                count_of_seconds)))
        elif count_of_minutes<10:
            canvas.itemconfigure(canvas_text, text="0" + str(count_of_minutes) + ":" + str(
            count_of_seconds))
        else:
            canvas.itemconfigure(canvas_text, text=str(count_of_minutes) + ":" + str(
                count_of_seconds))

        global timer
        timer=screen.after(1000, count_down, count_of_seconds - 1, count_of_minutes) # Continues timer after a pause of 1000 milliseconds



# ---------------------------- UI SETUP -------------------------------

# Setting up the screen
screen=Tk()
screen.title("pomodoro")
screen.minsize(width=500,height=300)
screen.config(pady=100,padx=50,background=GREEN)

#Setting up the canvas
canvas=Canvas(height=250,width=250)
canvas.configure(background=GREEN,highlightthickness=0)
image_from_file=PhotoImage(file="tomato.png")#this gets the image from the file
canvas.create_image(130,100,image=image_from_file)
canvas_text=canvas.create_text(130,120,text="00:00",font=(FONT_NAME,40,"bold"),fill="white")
canvas.grid(row=1,column=1)


#designing the buttons: start and reset
start=Button(text="Start",font=("Ariel",12,"bold"),command=start_clicked)
start.grid(row=3,column=0)

reset=Button(text="Reset",font=("Ariel",12,"bold"),command=reset_timer)
reset.grid_configure(column=3,row=3)

#Setting up a label
Timer=Label(text="Timer",font=("Ariel",24,"bold"),background=GREEN)
Timer.grid_configure(column=1,row=0,pady=25)

#Setting up the check mark symbol
Check_mark=Label(text="",background=GREEN,foreground="purple",font=("Ariel",20,"bold"))
Check_mark.grid(row=5,column=1,pady=25)


screen.mainloop() # Runs every millisecond to check for changes the GUI.
