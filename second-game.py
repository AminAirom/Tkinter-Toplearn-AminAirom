# ================================imports=============================
from tkinter import *
import tkinter.messagebox
import random

# =========================settings===================================
root = Tk()
root.title('Gola ya pooch')
root.geometry('270x280')
root.resizable(width=False, height=False)
color = '#43f7dc'
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
btn_1 = Button(Top_frist, text="daste rast", width=30, highlightbackground=color, command=lambda: rast())
btn_1.pack(side=LEFT, padx=5, pady=5)
btn_2 = Button(Top_second, text="daste chap", width=30, highlightbackground=color, command=lambda: chap())
btn_2.pack(side=LEFT, padx=5, pady=5)
btn_3 = Button(Top_forth, text="", width=30, highlightbackground=color)
btn_3.pack(side=LEFT, padx=5, pady=5)
btn_4 = Button(Top_six, text="", width=30, highlightbackground=color)
btn_4.pack(side=LEFT, padx=5, pady=5)
btn_5 = Button(Top_seven, text="clear", width=5, highlightbackground=color, command=lambda: clear())
btn_5.pack(side=LEFT, padx=5, pady=5)
btn_6 = Button(Top_eight, text="creator", width=5, highlightbackground=color, command=lambda: creator())
btn_6.pack(side=LEFT, padx=5, pady=5)


# ==========================functions==================================
def rast():
    z = random.randint(0, 1)
    if z == 0:
        btn_3['text'] = "gol!"
        btn_4['text'] = "You Win!"
    elif z == 1:
        btn_3['text'] = "pooch"
        btn_4['text'] = "You Lose!"


def chap():
    z = random.randint(0, 1)
    if z == 0:
        btn_3['text'] = "gol!"
        btn_4['text'] = "You Win!"
    elif z == 1:
        btn_3['text'] = "pooch"
        btn_4['text'] = "You Lose!"


def clear():
    btn_3["text"] = ""
    btn_4["text"] = ""


def creator():
    tkinter.messagebox.showinfo("CREATOR", "this game has been created by Amin Airom")


# ============================Enteries and Labels======================
d = Label(Top_five, text="Result:", bg=color)
d.pack(side=LEFT, padx=5, pady=5)
g = Label(Top_third, text="Computer Move:", bg=color)
g.pack(side=LEFT, padx=5, pady=5)
# ============================run======================================
root.mainloop()