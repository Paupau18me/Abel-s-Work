import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font

def captarHuellaWindow():
    huella_window = tk.Tk()
    huella_window.configure(background="#ebac00")
    huella_window.geometry("1200x600")


    tk.Label(huella_window, text="SISTEMA DE RECONOCIMENTO DE PATRONES DACTILARES", bg='#ebac00',
             font=("Arial", "24", "bold italic")).place(x=233,y=30)
    tk.Label(huella_window, text="BASADO EN LA TEORIA DE DERMATOGLIFIOS, PARA DETERMINAR", bg='#ebac00',
             font=("Arial", "24", "bold italic")).place(x=196, y=60)
    tk.Label(huella_window, text="LOS TALENTOS Y CAPACIDADES GENÉTICAS DE LOS DEPORTISTAS", bg='#ebac00',
             font=("Arial", "24", "bold italic")).place(x=189, y=90)



    tk.LabelFrame(huella_window, bg='black', height=350, width=1150).place(relx=0.5, rely=0.5, anchor=tk.CENTER,y=35)

    tk.LabelFrame(huella_window, bg='#EB5E00', height=319, width=325).place(x=36,y=175)

    # MANOSFRAME(Problemas)
    #   imageHuella = tk.PhotoImage(file="image/manos-4.gif")
    #   l = tk.Label(huella_window, image=imageHuella).place(x=36, y=36)


    '''
    #BTNGuardar
    btn_guardar = tk.Button(
        huella_window,
        highlightbackground='yellow',
        text='GUARDAR',
        font=('Arial Rounded MT Bold', 14),
        width=20
        #   command = guardar
    ).place(x=200, y=900)

    # btnResultados
    btn_resultados = tk.Button(
        huella_window,
        highlightbackground='yellow',
        text='Resultados',
        font=('Arial Rounded MT Bold', 14),
        width=20
        #   command = resultados
    ).place(x=250, y=1000)

    # Btn Volver
    btn_volver = tk.Button(
        huella_window,
        highlightbackground='yellow',
        text='Volver',
        font=('Arial Rounded MT Bold', 14),
        width=20
        # command = huella_window.destroy()
    ).place(x=300, y=1100)
    
    '''


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
    highlightbackground='#FBFF00',
    text = 'CARTA DERMATOGLÍFIA',
    font = ('Arial Rounded MT Bold', 14),
    width = 20
    #   command = resultsWindow
).place(x = 50, y = 60)

#CONFIGURACION
btn_configuracion = tk.Button(
    window,
    highlightbackground='#04FEEF',
    text = 'CONFIGURACIÓN',
    font = ('Arial Rounded MT Bold', 14),
    width = 20
    #   command = configuracionWindow
).place(x = 855, y = 60)

#CAPTAR HUELLA
btn_huella = tk.Button(
    window,
    highlightbackground='#08FE04',
    text = 'CAPTAR HUELLA',
    font = ('Arial Rounded MT Bold', 14),
    width = 20,
    command = captarHuellaWindow
).place(x = 1075, y = 60)


#Acerca del autor
btn_author = tk.Button(
    window,
    highlightbackground='#FFC638',
    text = 'ACERCA DEL AUTOR',
    font = ('Arial Rounded MT Bold', 14),
    width = 20
    #   command = autorWindow
).place(x = 1075, y = 550)

#Volver
btn_volver = tk.Button(
    window,
    highlightbackground='#FFC638',
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