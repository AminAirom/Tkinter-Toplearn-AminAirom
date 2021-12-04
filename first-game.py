# ================================imports=============================
from tkinter import *
import tkinter.messagebox
import random

# =========================settings===================================
root = Tk()
root.title('Rock,Paper,Scissor')
root.geometry('270x280')
root.resizable(width=False, height=False)
color = '#31f784'
root.configure(bg=color)
# ==========================Frames====================================
Top_frist = Frame(root, width=400, height=50, bg=color)
Top_frist.pack(side='top')

Top_second = Frame(root, width=400, height=50, bg=color)
Top_second.pack(side='top')

Top_third = Frame(root, width=400, height=50, bg=color)
Top_third.pack(side='top')

Top_forth = Frame(root, width=400, height=50, bg=color)
Top_forth.pack(side='top')

Top_five = Frame(root, width=400, height=50, bg=color)
Top_five.pack(side='top')

Top_six = Frame(root, width=400, height=50, bg=color)
Top_six.pack(side='top')

Top_seven = Frame(root, width=400, height=50, bg=color)
Top_seven.pack(side='top')

Top_eight = Frame(root, width=400, height=50, bg=color)
Top_eight.pack(side='top')

# ==========================buttons===================================
btn_1 = Button(Top_frist, text="Rock", width=30, highlightbackground=color, command=lambda: rock())
btn_1.pack(side=LEFT, padx=5, pady=5)
btn_2 = Button(Top_second, text="Paper", width=30, highlightbackground=color, command=lambda: paper())
btn_2.pack(side=LEFT, padx=5, pady=5)
btn_3 = Button(Top_third, text="Scissor", width=30, highlightbackground=color,command=lambda: scissor())
btn_3.pack(side=LEFT, padx=5, pady=5)
btn_4 = Button(Top_seven, text="", width=30, highlightbackground=color)
btn_4.pack(side=LEFT, padx=5, pady=5)
btn_5 = Button(Top_eight, text="creator", width=5, highlightbackground=color, command=lambda: creator())
btn_5.pack(side=LEFT, padx=5, pady=5)
btn_6 = Button(Top_eight, text="clear", width=5, highlightbackground=color, command=lambda:clear())
btn_6.pack(side=LEFT, padx=5, pady=5)
btn_7 = Button(Top_five, text="", width=30, highlightbackground=color)
btn_7.pack(side=LEFT, padx=5, pady=5)


# ==========================functions==================================
def creator():
    tkinter.messagebox.showinfo("CREATOR", "this game has been created by Amin Airom")


def rock():
    z = random.randint(0, 2)
    if z == 0:
        btn_7['text'] = "Rock"
        btn_4['text'] = "Tie!"
    elif z == 1:
        btn_7['text'] = "Paper"
        btn_4['text'] = "You Lose!"
    elif z == 2:
        btn_7['text'] = "Scissor"
        btn_4['text'] = "You Win!"


def paper():
    z = random.randint(0, 2)
    if z == 0:
        btn_7['text'] = "Rock"
        btn_4['text'] = "You Win!"
    elif z == 1:
        btn_7['text'] = "Paper"
        btn_4['text'] = "Tie!"
    elif z == 2:
        btn_7['text'] = "Scissor"
        btn_4['text'] = "You Lose!"

def scissor():
    z = random.randint(0, 2)
    if z == 0:
        btn_7['text'] = "Rock"
        btn_4['text'] = "You Lose!"
    elif z == 1:
        btn_7['text'] = "Paper"
        btn_4['text'] = "You Win!"
    elif z == 2:
        btn_7['text'] = "Scissor"
        btn_4['text'] = "Tie!"

def clear():
    btn_7['text'] = ""
    btn_4['text'] = ""

# ============================Enteries and Labels======================
d = Label(Top_six, text="Result:", bg=color)
d.pack(side=LEFT, padx=5, pady=5)
g = Label(Top_forth, text="Computer Move:", bg=color)
g.pack(side=LEFT, padx=5, pady=5)
# ============================run======================================
root.mainloop()
