from tkinter import  *
from tkinter import ttk

from pygments.styles.dracula import background, foreground
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

# cores
color1 = "#3b3b3b" # black - escuro
color2 = "#333"     # black - claro
color3 = "#fff"     # white
color4 = "#fcc058"  # orange

window = Tk()
window.title('Age calculator')
window.geometry('310x410')
window.config(bg=color1)

style = ttk.Style(window)
style.theme_use("clam")

#Frames
top_frame = Frame(
    window, width=310, height=140, pady=0, padx=0, relief="flat", bg=color2
)
top_frame.grid(row=0, column=0)

bottom_frame = Frame(
    window, width=310, height=140, pady=0, padx=0, relief="flat", bg=color2
)
bottom_frame.grid(row=1, column=0, sticky=NW)

#Lables Top Frame
app_calculator = Label(
    top_frame, text="Calcula Idade", width=25, height=1,
    padx=3, relief="flat", anchor="center", font=("Ivy 15 bold"),
    bg=color2, fg=color3)

app_calculator.place(x=0, y=30)

app_of_rage = Label(
    top_frame, text="Age", width=11, height=1,
    padx=0, relief="flat", anchor="center", font=("Arial 35 bold"),
    bg=color2, fg=color4
)

app_calculator.place(x=0, y=70)

initial_date = Label(bottom_frame, text="Data Inicial", height=1, padx=0, pady=0,
                     relief="flat", anchor=NW, font=("Ivy 9"), bg=color1, fg=color3)
initial_date.place(x=50, y=30)

calc_initial_date = DateEntry(bottom_frame, width=10, background="darkblue", foreground="white",
                              borderwidth=2, datepattern="dd/mm/y", year=2025)
calc_initial_date.place(x=170, y=30)


window.mainloop()

