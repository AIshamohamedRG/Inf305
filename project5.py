from tkinter import *
from tkinter import ttk
import datetime

aisha = Tk()
aisha.geometry('350x300')
aisha.title('student project')

def msg():
    n = cm.get()
    if n == 'Year':
        lbl.config(text=datetime.date.today().year)
    elif n == 'Day':
        lbl.config(text=datetime.date.today().day)
    elif n == 'Month':
        lbl.config(text=datetime.date.today().month)
    elif n == 'Hour':
        lbl.config(text=datetime.datetime.now().hour)
    elif n == 'Minute':
        lbl.config(text=datetime.datetime.now().minute)
    elif n == 'Second':
        lbl.config(text=datetime.datetime.now().second)

lbl = Label(aisha, text = '', font=('Courier', 25, 'bold'))
lbl.place(x=310, y=20) 
btn = Button(aisha, text = 'Show Date/Time', font=(20), width=22, command=msg)
btn.place(x=5, y=200)

cm = ttk.Combobox(aisha, font=(10))
cm.place(x=5, y=10)
cm["values"] = tuple(['Day', 'Month', 'Year', 'Hour', 'Minute', 'Second'])

aisha.mainloop()