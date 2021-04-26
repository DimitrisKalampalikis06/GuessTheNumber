from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import tkinter as tk
from tkinter.ttk import *
import random
import time
from tkinter import font

root = Tk()
root.configure(background='black')
root.geometry('600x560')
root.title('The Number Game')

logo = PhotoImage(file="upvote.png")
logo2 = PhotoImage(file="downvote.png")
logo3 = PhotoImage(file="check.png")
a = random.randint(0, 100)
b = 0
c = 0
d = 0
h = 0
t = 0
r = 0
g = 0
l = 0
p = random.randint(0, 100)
progr = IntVar()
s = Style()


def effect():
    global lbl5, p, h
    if h == 0:
        lbl5 = tk.Label(root, text='', fg='#B21D1D', bg='black', font=('Tahoma', 25))
        lbl5.grid(row=6, column=0, columnspan=2)

    for i in range(15):
        lbl5.configure(text=p)
        lbl5.update()
        p = random.randint(0, 100)
        time.sleep(0.1)
    lbl5.configure(text='The number is ready')


def restart():
    global a, lbl33, b, c, progr, t, r, l
    t = 0
    r = 0
    l = 0
    lbl334.configure(text='Tries:' + str(r),fg='white')
    lbl334.update()
    if c == 0:
        lbl3.destroy()
        c = 1
    else:
        lbl33.destroy()
    progr.set(0)
    a = random.randint(0, 100)
    entr.configure(state='normal')
    entr.delete(0, 'end')
    b = 2
    lbl33 = tk.Label(root, text='Make a guess', fg='white', bg='black', font=('Tahoma', 25), pady=44)
    lbl33.grid(row=2, column=1)
    lbl5.destroy()
    effect()
    root.bind('<Return>', go)


def go(*args):
    global a, b, progr, d, t, r, g, l
    if b == 0:
        entr.configure(state='normal')
        btn2.configure(state='normal')
        b = 1
        effect()
    elif b == 1:
        t = 1
        if entr.get().isdecimal() == True and int(entr.get()) >= 0 and int(entr.get()) <= 100:
            if int(entr.get()) == a:
                lbl3.configure(image=logo3)
                entr.configure(state="disabled")
                r += 1
                if r <= 3:
                    lbl334.configure(text='Tries:' + str(r), fg='green')
                elif r > 3 and r <= 7:
                    lbl334.configure(text='Tries:' + str(r), fg='orange')
                else:
                    lbl334.configure(text='Tries:' + str(r), fg='red')
                lbl334.update()
                l = 1
                g = r
                lbl333.configure(text='Highscore:' + str(g))
                lbl333.update()
            elif int(entr.get()) > a:
                lbl3.configure(image=logo2)
            elif int(entr.get()) < a:
                lbl3.configure(image=logo)
            d = int(entr.get())
            if l == 0:
                r += 1
                if r<=3:
                    lbl334.configure(text='Tries:' + str(r),fg='green')
                elif r>3 and r<=7:
                    lbl334.configure(text='Tries:' + str(r), fg='orange')
                else:
                    lbl334.configure(text='Tries:' + str(r), fg='red')
                lbl334.update()
            progr.set(d)
        else:
            messagebox.showerror('ERROR', message='Only numbers between 0 and 100')
    elif b == 2:
        t = 1
        if entr.get().isdecimal() == True and int(entr.get()) >= 0 and int(entr.get()) <= 100:
            if int(entr.get()) == a:
                lbl33.configure(image=logo3)
                entr.configure(state="disabled")
                r += 1
                if r <= 3:
                    lbl334.configure(text='Tries:' + str(r), fg='green')
                elif r > 3 and r <= 7:
                    lbl334.configure(text='Tries:' + str(r), fg='orange')
                else:
                    lbl334.configure(text='Tries:' + str(r), fg='red')
                lbl334.update()
                l = 1
                if r < g:
                    g = r
                    lbl333.configure(text='Highscore:' + str(g))
                    lbl333.update()
            elif int(entr.get()) > a:
                lbl33.configure(image=logo2)
            elif int(entr.get()) < a:
                lbl33.configure(image=logo)
            d = int(entr.get())
            if l == 0:
                r += 1
                if r <= 3:
                    lbl334.configure(text='Tries:' + str(r), fg='green')
                elif r > 3 and r <= 7:
                    lbl334.configure(text='Tries:' + str(r), fg='orange')
                else:
                    lbl334.configure(text='Tries:' + str(r), fg='red')
                lbl334.update()
            progr.set(d)
        else:
            messagebox.showerror('ERROR', message='Only numbers between 0 and 100')
    entr.delete(0, 'end')
    if t == 1:
        lbl5.destroy()


def menuu():
    global lbl, logo, logo2, logo3, lbl2, lbl3, entr, btn, btn2, a, progr, bar, s, r, s, lbl334, lbl333
    lbl = tk.Label(root, text='Guess the number', fg='#41199C', bg='black', font=('Tahoma', 30), relief='sunken')
    lbl.grid(row=0, column=0, columnspan=2)
    f = font.Font(lbl, lbl.cget("font"))
    f.configure(underline=True)
    lbl.configure(font=f)
    lbl2 = tk.Label(root,
                    text='The player has to guess a number.\n The number will be between 0 and 100\nPress enter to start and guess',
                    fg='white', bg='black', font=('Helvetica', 20))
    lbl2.grid(row=1, column=0, columnspan=2)
    entr = tk.Entry(root, fg='black', bg='white', font=('Tahoma', 25), width=5, justify='center', state='disabled')
    entr.grid(row=2, column=0)
    lbl3 = tk.Label(root, text='Make a guess', fg='white', bg='black', font=('Tahoma', 25), pady=46)
    lbl3.grid(row=2, column=1)
    btn = tk.Button(root, text='Exit', command=quit, fg='white', bg='black', font=('Tahoma', 25))
    btn.grid(row=3, column=0)
    btn2 = tk.Button(root, text='Restart', command=restart, state='disabled', fg='white', bg='black',
                     font=('Tahoma', 25))
    btn2.grid(row=3, column=1)
    s.theme_use("default")
    s.configure("TProgressbar", thickness=30)
    bar = ttk.Progressbar(root, length=600, style='grey.Horizontal.TProgressbar', variable=progr)
    bar.grid(row=4, column=0, columnspan=2)
    lbl334 = tk.Label(root, text='Tries:' + str(r), fg='white', bg='black', font=('Tahoma', 25))
    lbl334.grid(row=5, column=0)
    lbl333 = tk.Label(root, text='Highscore:' + str(g), fg='white', bg='black', font=('Tahoma', 25))
    lbl333.grid(row=5, column=1)
    root.bind('<Return>', go)


menuu()
root.mainloop()
