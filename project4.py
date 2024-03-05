from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

aisha = Tk()
aisha.geometry('400x300')
aisha.title('Student Project')

def msg():
    n = cm.get()
    if n == 'Cat':
        img = Image.open('cat.jpg')
    elif n == 'Dog':
        img = Image.open('dog.jpg')
    elif n == 'Bird':
        img = Image.open('bird.jpg')

    img = img.resize((300, 280))  
    img = ImageTk.PhotoImage(img)  
    lbl.configure(image=img)
    lbl.image = img  

lbl = Label(aisha)
lbl.place(x=300, y=10)
btn = Button(aisha, text='Show Image', font=('Arial', 12), width=15, command=msg)
btn.place(x=50, y=250)

cm = ttk.Combobox(aisha, font=('Arial', 12))
cm.place(x=50, y=10)
cm['values'] = ('Cat', 'Dog', 'Bird')

aisha.mainloop()