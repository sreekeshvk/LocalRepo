# importing tkinter 

from tkinter import*;
from tkinter.filedialog import*;

# creating text box design

win = Tk()
win.geometry('400x570')
win.title('PyDocs')

text = Text(win,font='impack 15 ',bg='white',wrap=WORD)
text.pack(padx=1,pady=30)


# open file function

def openfile():
    file = askopenfile(mode='r',filetypes=[('filename','*.txt')])
    if file is not None:
        content = file.read()
        text.insert(INSERT,content)    


# save file function

def save():
    new_file = asksaveasfile(mode='w',filetypes=[('filename','.txt')])
    if new_file is None:
        return
    textDocs = text.get(1.0,END)
    new_file.write(textDocs)
    new_file.close()


# clear all function

def clearAll():
    text.delete(1.0,END )

# Button 1: save text

Button(
    win,
    text='save',
    font=('Segoe UI', 10),
    fg='black',
    bg='SystemButtonFace',
    activebackground='lightgrey',
    activeforeground='black',
    borderwidth=1,
    relief='flat',
    cursor='arrow',
    command=save
).place(x=10, y=0)

# Button 2: open files

Button(
    win,
    text='open',
    font=('Segoe UI', 10),
    fg='black',
    bg='SystemButtonFace',
    activebackground='lightgrey',
    activeforeground='black',
    borderwidth=1,
    relief='flat',
    cursor='arrow',
    command=openfile
).place(x=60, y=0)

# Button 3: clear all

Button(
    win,
    text='clear',
    font=('Segoe UI', 10),
    fg='black',
    bg='SystemButtonFace',
    activebackground='lightgrey',
    activeforeground='black',
    borderwidth=1,
    relief='flat',
    cursor='arrow',
    command=clearAll
).place(x=110, y=0)


mainloop()
