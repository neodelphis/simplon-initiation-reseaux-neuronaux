from tkinter import *

global old_x, old_y
old_x = None
old_y = None


def clear_canvas():
    canevas.delete('all')


def paint(event):
    global old_x, old_y
    if old_x and old_y:
        canevas.create_line(old_x, old_y, event.x, event.y,
                            width=10, fill='black',
                            capstyle=ROUND, smooth=TRUE, splinesteps=36)
    old_x = event.x
    old_y = event.y


def reset(event):
    global old_x, old_y
    old_x, old_y = None, None


fenetre = Tk()
fenetre.title('Reconnaissance')


canevas = Canvas(fenetre, bg='white', width=200, height=200)
canevas.pack()

clear_button = Button(fenetre, text='Effacer', command=clear_canvas)
clear_button.pack(expand=YES, fill=BOTH)

# Bouton à coder
save_button = Button(fenetre, text='Sauvegarder')
save_button.pack(expand=YES, fill=BOTH)

canevas.bind('<B1-Motion>', paint)
canevas.bind('<ButtonRelease-1>', reset)

fenetre.mainloop()
