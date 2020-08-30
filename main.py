import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font

def captarHuellaWindow():
    huella_window = tk.Tk()
    tk.Label(window, text='Hola Mundo :3')
    huella_window.resizable(width=False, height=False)
    huella_window.mainloop()

window = tk.Tk()
'''
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
#window.geometry('{}x{}'.format(screen_width,screen_height))
#print('{} x {}'.format(screen_width,screen_height))
'''


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # avoid garbage collection

image = Image.open('image/fondo10.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = tk.Label(window, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=tk.BOTH, expand=tk.YES)


#EMI FRAME

imageEmi= tk.PhotoImage(file="image/emi400px.png")
labelEmi= tk.Label(window, image= imageEmi).place(x=855,y=100)

#CARTA DERMATOGLIFIA
btn_resultados = tk.Button(
    window,
    text = 'CARTA DERMATOGLÍFIA',
    font = ('Arial Rounded MT Bold', 14),
    width = 20
    #   command = resultsWindow
).place(x = 50, y = 60)

#CONFIGURACION
btn_configuracion = tk.Button(
    window,
    text = 'CONFIGURACIÓN',
    font = ('Arial Rounded MT Bold', 14),
    width = 20
    #   command = configuracionWindow
).place(x = 855, y = 60)

#CAPTAR HUELLA
btn_huella = tk.Button(
    window,
    text = 'CAPTAR HUELLA',
    font = ('Arial Rounded MT Bold', 14),
    width = 20,
    command = captarHuellaWindow
).place(x = 1075, y = 60)


#Acerca del autor
btn_author = tk.Button(
    window,
    text = 'ACERCA DEL AUTOR',
    font = ('Arial Rounded MT Bold', 14),
    width = 20
    #   command = autorWindow
).place(x = 1075, y = 550)

#Volver
btn_volver = tk.Button(
    window,
    text = 'VOLVER',
    font = ('Arial Rounded MT Bold', 14),
    width = 20
    #   command = autorWindow
).place(x = 1075, y = 600)

#FUENTES DISPONIBLES
'''
from tkinter import font

for font in font.families():
    print(font)
'''

#window.resizable(width=False, height=False)
window.mainloop()