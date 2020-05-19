from tkinter import *
from PIL import Image, ImageDraw

global old_x, old_y
old_x = None
old_y = None


def clear_canvas():
    canevas.delete('all')
    calque.rectangle((0, 0, 200, 200), fill='white')
    etiquette.config(text=' ')


def reco_canvas():
    # Sauvegarde en une image (28, 28)
    # image_resized = image.resize((28, 28))
    # image_resized.save('image-test.png')
    etiquette.config(text='?')


def paint(event):
    global old_x, old_y
    if old_x and old_y:
        canevas.create_line(old_x, old_y, event.x, event.y,
                            width=15, fill='black',
                            capstyle=ROUND, smooth=TRUE, splinesteps=36)
        calque.line((old_x, old_y, event.x, event.y), width=15, fill='black')
    old_x = event.x
    old_y = event.y


def reset(event):
    global old_x, old_y
    old_x, old_y = None, None


fenetre = Tk()
fenetre.title('Reconnaissance')


canevas = Canvas(fenetre, bg='white', width=200, height=200)
canevas.pack()

# Copie de l'image à l'écran via PIL
# L'image est crée en mémoire
image = Image.new('L', (200, 200), 'white')
# Le calque permet de suivre les même étapes que ce qui est fait à l'écran
calque = ImageDraw.Draw(image)


save_button = Button(fenetre, text='Reconnaître', command=reco_canvas)
save_button.pack(expand=YES, fill=BOTH)

# Creation d'une étiquette
etiquette = Label(fenetre)
etiquette.pack()


clear_button = Button(fenetre, text='Effacer', command=clear_canvas)
clear_button.pack(expand=YES, fill=BOTH)

canevas.bind('<B1-Motion>', paint)
canevas.bind('<ButtonRelease-1>', reset)

fenetre.mainloop()
