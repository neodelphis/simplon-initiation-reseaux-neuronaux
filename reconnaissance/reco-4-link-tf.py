from tkinter import *
from PIL import Image, ImageDraw
import tensorflow.keras
import numpy as np

global old_x, old_y
old_x = None
old_y = None

# Le réseau entraîné
loaded_model = tensorflow.keras.models.load_model('../model_mnist')


def clear_canvas():
    canevas.delete('all')
    calque.rectangle((0, 0, 200, 200), fill='white')
    etiquette.config(text=' ')


def reco_canvas():
    # Conversion en une image (28, 28)
    image_resized = image.resize((28, 28))
    x_test = np.asarray(image_resized)
    x_test = x_test.reshape(1, 28, 28, 1)
    x_test = x_test / 255.
    valeur = loaded_model.predict_classes(x_test)[0]
    etiquette.config(text=str(valeur))


def paint(event):
    global old_x, old_y
    if old_x and old_y:
        canevas.create_line(old_x, old_y, event.x, event.y,
                            width=25, fill='black',
                            capstyle=ROUND, smooth=TRUE, splinesteps=36)
        calque.line((old_x, old_y, event.x, event.y), width=25, fill='black')
    old_x = event.x
    old_y = event.y


def reset(event):
    global old_x, old_y
    old_x, old_y = None, None


fenetre = Tk()
fenetre.title('Reconnaissance')

canevas = Canvas(fenetre, bg='white', width=200, height=200)
canevas.pack()
canevas.bind('<B1-Motion>', paint)
canevas.bind('<ButtonRelease-1>', reset)

save_button = Button(fenetre, text='Reconnaître', command=reco_canvas)
save_button.pack(expand=YES, fill=BOTH)

# Creation d'une étiquette
etiquette = Label(fenetre)
etiquette.pack()

clear_button = Button(fenetre, text='Effacer', command=clear_canvas)
clear_button.pack(expand=YES, fill=BOTH)


# Copie de l'image à l'écran via PIL
# L'image est crée en mémoire
image = Image.new('L', (200, 200), 'white')
# Le calque permet de suivre les même étapes que ce qui est fait à l'écran
calque = ImageDraw.Draw(image)


fenetre.mainloop()
