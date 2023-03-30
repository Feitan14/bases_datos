from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import * #1. presentamos los archivos controlodador vista

#2. creamos un objeto de clase controlador
controlador = controladorBD()

#3. funcion para disparar un boton
def ejecutaIntsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

#3.1 funcion para disparar un boton de busqueda
def ejecutaSelectU():
    usuario = controlador.consultarUsuario(varBus.get())
    
    for usu in usuario:
        cadena = str(usu[0])+ " "+usu[1]+ " " +usu[2]+ " " +str(usu[3])
        print(cadena)
        if (usuario)
        print(cadena)
    else:
        messagebox.showinfo("No encontrado","Ese usuario no existe en la BD")
        

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

#agregamos las variables
varNom =tk.StringVar()
lblNom = Label(pestana1, text= "nombre: ").pack()
textNom = Entry(pestana1, textvariable=varNom).pack()

varCor =tk.StringVar()
lblCor = Label(pestana1, text= "Correo: ").pack()
textCor = Entry(pestana1, textvariable=varCor).pack()

varCon =tk.StringVar()
lblCon = Label(pestana1, text= "Contraseña: ").pack()
textCon = Entry(pestana1, textvariable=varCon).pack()

btnGuardar = Button(pestana1, text="Guardar Usuario",command=ejecutaIntsert).pack()

#Pestaña 2:Buscar suarios

titulo2 = Label(pestana2, text="Buscar usuarios", fg='green', font=('Modern',18)).pack()

#agregamos las variables

varBus =tk.StringVar()
lblid = Label(pestana2, text= "Identificar usuario: ").pack()
textid = Entry(pestana2, textvariable=varBus).pack()
btnBus = Button(pestana2, text="Buscar",command=ejecutaSelectU).pack()

subBus = Label(pestana2,text="Encontrado", fg='blue',font=('Modern',15)).pack()
textEnc = tk.Text(pestana2,height=5, width=52).pack()

#agregamos los textos que iran dentro de las pestañas

panel.add(pestana1, text='Formulario de usuario')
panel.add(pestana2, text='Buscar usuario')
panel.add(pestana3, text='consultar usuarios')
panel.add(pestana4, text='Actualizar usuario')

ventana.mainloop()