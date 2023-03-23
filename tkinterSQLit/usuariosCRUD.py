from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana = Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("420x300")

panel = ttk.Notebook(ventana)
panel.pack(fill ='both',expand='yes')

#agregamos los paneles que tendran forma en la ventana
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

titulo = Label(pestana1, text="Registro de usuarios", fg='blue', font=('Modern',18)).pack()

varNom =tk.StringVar()
lblNom = Label(pestana1, text= "nombre: ").pack()
textNom = Entry(pestana1, textvariable=varNom).pack()

varCor =tk.StringVar()
lblCor = Label(pestana1, text= "Correo: ").pack()
textCor = Entry(pestana1, textvariable=varCor).pack()

varCon =tk.StringVar()
lblCon = Label(pestana1, text= "Contraseña: ").pack()
textCon = Entry(pestana1, textvariable=varCon).pack()

btnGuardar = Button(pestana1, text="Guardar Usuario").pack()

#agregamos los textos que iran dentro de las pestañas
panel.add(pestana1, text='Formulario de usuario')
panel.add(pestana2, text='Buscar usuario')
panel.add(pestana3, text='consultar usuarios')
panel.add(pestana4, text='Actualizar usuario')

ventana.mainloop()