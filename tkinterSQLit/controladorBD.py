from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    def __init__(self):
        pass
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/andy2/OneDrive/Documentos/GitHub/bases_datos/tkinterSQLit/DBUsuarios.db")
            print("conectado a la BD")
            return conexion 
        #
        except sqlite3.OperationalError:
            print("no se pudo conectar")

#metodos para guardar usuarios
    def guardarUsuario(self, nom, cor, con):
        
        #1.primer paso para guardar usuario, usamos una conexion
        conx = self.conexionBD()
        
        #2. validamos los parametros que no esten vacios
        if(nom == "" or cor == "" or con == "" ):
            messagebox.showwarning("Cuidado","Formulario Incompleto")
            
        else:
            #preparamos 3 cosas;
            #el Cursor, Datos y QuerySQL
            cursor = conx.cursor()
            conH = self.encriptarCon(con)
            datos = (nom,cor,conH)
            qrInsert = "insert into TNRegistados(nombre,correo,contraseña) values(?,?,?)"
            
            #4. Ejecutar Insert y cerramos conexion
            cursor.execute(qrInsert,datos) 
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario Guardado")
    #Metodo para encriptar contraseñas
    def encriptarCon(self,con):
        conPlana = con
        conPlana = conPlana.encode() #convertimos con a bytes
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(conPlana,sal)
        print(conHa)        
        
        #enviamos la contraseña incriptada
        return conHa
        
            #Metodo para buscar 1 usuario
    
    def consultarUsuario(self,id):
        # 1. preparar una conexion
        conx = self.conexionBD()
        #2. verificar si el parametro id contiene algo
        if(id == ""):
            messagebox.showwarning("cuidado id vacio, escribe algo valido")
            conx.close()
        else:
            try:
                #3. preparamos lo necesario, cursor y query
                cursor = conx.cursor()
                selectQry = "selec * from TBRegistrados where id = "+id
                #4. ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsUsuario = cursor.fetchall()
                conx.close()
                return rsUsuario
            
            except sqlite3.OperationalError:
                print("error consulta")