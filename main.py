import os
import random
import tkinter.ttk
from tkinter import *

from setuptools._distutils.command.config import config

from Dominio.Inventario import Inventario
from Dominio.Player import Player
from Dominio.Partida import Partida
from Dominio.Ayudante import Ayudante

from Infraestructura.Persistencia import Persistencia
saver = Persistencia()
saver.connect()
inventario = Inventario()


ventana = Tk()
ventana.geometry("400x300")
ventana.eval('tk::PlaceWindow . center')
playerGlobal = ""
contador = 0
contFaciles = 0
contMedio = 0
contDificiles = 0
contPremio=0
contPremioSeguro = 0
cant = 0
arrayFinal = []
ventana.title("Quien Quiere Ser Millonario")

etiqueta = Label(ventana,text="Quien Quiere Ser Millonario", bg="blue" , fg="white", font="Roman")


#hola = Label(ventana,text="Hola",bg="black",fg="white")

#etiqueta.pack(fill = tkinter.Y, expand=True) Expandir en Y
#etiqueta.pack(fill = tkinter.BOTH, expand=True)  Expandir por toda la pantalla
etiqueta.pack(fill = X)  #Expandir en X
#hola.pack(fill = X)
#print(list(tkFont.families()))

def cargar_file():

    global player
    global contador
    global contFaciles
    global contMedio
    global contDificiles
    global arrayFinal
    global contPremio
    global contPremioSeguro
    global cant

    inventario.eliminar_listas()
    for file in os.listdir("./Files"):
        if '.json' in file:
            inventario.agregar_objeto(saver.load_json(file))



def close_window():
    ventana.destroy()

def gano(playerGlobal):
    cargar_file()
    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')
    lblFelicitaciones = Label(frame, text="Felicitaciones: "+playerGlobal.nombre +" "+playerGlobal.apellido+"\nHas Ganado", font="Roman")
    lblFelicitaciones.place(relx=0.1, rely=0.05)

    lblPremio = Label(frame,text="Premio :"+str(contPremio),font="Roman")
    lblPremio.place(relx=0.1, rely=0.35)

    cedula_player = playerGlobal.cedula

    partida = Partida(cedula_player, contPremio, contador)
    saver.save_json(partida)

    def abrirJuego():
        juego(playerGlobal)
        frame.destroy()

    salir = Button(frame, text="Salir", bg="blue", fg="white", font="Roman", command=abrirJuego)
    salir.place(relx=0.45, rely=0.7, relwidth=0.2, relheight=0.15)

def perdio(playerGlobal):
    ventana.geometry("400x300")
    cargar_file()
    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')
    lblLamento = Label(frame,text="Lo Lamento: " + playerGlobal.nombre + " " + playerGlobal.apellido + "\nHas Perdido",font="Roman")
    lblLamento.place(relx=0.1, rely=0.05)

    lblPremio = Label(frame, text="Premio : " + str(contPremioSeguro), font="Roman")
    lblPremio.place(relx=0.1, rely=0.35)

    cedula_player = playerGlobal.cedula

    partida = Partida(cedula_player,contPremioSeguro,contador)
    saver.save_json(partida)

    def abrirJuego():
        juego(playerGlobal)
        frame.destroy()


    salir = Button(frame, text="Salir", bg="blue", fg="white", font="Roman" , command=abrirJuego)
    salir.place(relx=0.45, rely=0.7, relwidth=0.2, relheight=0.15)

def preguntas(playerGlobal,cant):
    global contador,contPremioSeguro,contPremio
    ventana.geometry("600x300")
    cargar_file()
    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')
    lblPregunta = Label(frame, text="Pregunta "+str((contador+1))+":", font="Roman")
    lblPregunta.place(relx=0.1, rely=0.05)

    Seguro = Label(frame, text="", font="Roman")
    Seguro.place(relx=0.1, rely=0.15)

    eleccion=""

    if cant == 10:
        if contador == 3 or contador==6 or contador==9:
            contPremioSeguro = contPremio

        if contador == 2 or contador == 5 or contador == 8:
            Seguro['text'] = "Pregunta Seguro"




    if cant == 11:
        if contador == 4 or contador == 7 or contador == 10:
            contPremioSeguro = contPremio

        if contador == 3 or contador == 6 or contador == 9:
            Seguro['text'] = "Pregunta Seguro"

    if cant == 16:
        if contador == 5 or contador == 10 or contador == 15:
            contPremioSeguro = contPremio

        if contador == 4 or contador == 9 or contador == 14:
            Seguro['text'] = "Pregunta Seguro"

    def elecciona():
        global contador, contPremio,contPremioSeguro

        eleccion = a['text']
        res=pre.respuesta
        if eleccion==res:


            print("Bien hecho")
            contPremio += pre.valor
            print("Premio: "+str(contPremio))
            frame.destroy()
            contador += 1



            if (contador == len(arrayFinal)):
                gano(playerGlobal)

                frame.destroy()
            else:
                preguntas(playerGlobal, cant)
                frame.destroy()

        else:
            perdio(playerGlobal)
            frame.destroy()
    def eleccionb():
        global contador, contPremio,contPremioSeguro

        eleccion = b['text']
        res = pre.respuesta
        if eleccion == res:


            print("Bien hecho")
            contPremio += pre.valor
            print("Premio: "+str(contPremio))
            frame.destroy()
            contador += 1
            #lblPremio['text'] = str(contPremio)
            if (contador == len(arrayFinal)):
                gano(playerGlobal)

                frame.destroy()
            else:
                preguntas(playerGlobal, cant)
                frame.destroy()

        else:
            perdio(playerGlobal)
            frame.destroy()
    def eleccionc():

        global contador, contPremio,contPremioSeguro

        eleccion = c['text']
        res = pre.respuesta
        if eleccion == res:


            print("Bien hecho")
            contPremio += pre.valor
            print("Premio: "+str(contPremio))
            frame.destroy()
            contador += 1
            #lblPremio['text'] = str(contPremio)
            if (contador == len(arrayFinal)):
                gano(playerGlobal)

                frame.destroy()
            else:
                preguntas(playerGlobal, cant)
                frame.destroy()

        else:
            perdio(playerGlobal)
            frame.destroy()

    def elecciond():
        global contador, contPremio,contPremioSeguro

        eleccion = d['text']
        res = pre.respuesta
        if eleccion == res:


            print("Bien hecho")
            contPremio += pre.valor
            print("Premio: "+str(contPremio))
            frame.destroy()
            contador += 1
            #lblPremio['text'] = str(contPremio)
            if (contador == len(arrayFinal)):
                gano(playerGlobal)
                frame.destroy()
            else:
                preguntas(playerGlobal, cant)
                frame.destroy()
        else:
            perdio(playerGlobal)
            frame.destroy()



    a = Button(frame, bg="blue", fg="white", font="Roman", command=elecciona)
    a.place(relx=0.2, rely=0.4, relwidth=0.2, relheight=0.15)

    b = Button(frame, bg="blue", fg="white", font="Roman",command=eleccionb)
    b.place(relx=0.2, rely=0.6, relwidth=0.2, relheight=0.15)

    c = Button(frame, bg="blue", fg="white", font="Roman",command=eleccionc)
    c.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.15)

    d = Button(frame, bg="blue", fg="white", font="Roman",command=elecciond)
    d.place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.15)




    cantidad = cant
    cantPre = len(inventario.preguntas)






    pre=arrayFinal[contador]
    lblPregunta['text'] += " "+ pre.pregunta

    a['text'] = pre.opcion_a
    b['text'] = pre.opcion_b
    c['text'] = pre.opcion_c
    d['text'] = pre.opcion_d









def cargarPreguntas(facil,medio,dificil):
    global contFaciles
    global contDificiles
    global contMedio
    arrayFinal.clear()
    total = facil+medio+dificil
    array = []

    for i in inventario.preguntas:
        array.append(i)



    for i in inventario.preguntas:

        if len(arrayFinal)<total:
            num = random.randint(0, len(array)-1)


            if array[num].dificultad == "Facil":

                if contFaciles<facil:
                    if len(arrayFinal) == 0:
                        arrayFinal.append(array[num])
                    else:
                        esta = False
                        for k in arrayFinal:
                            if k.codigo == i.codigo:
                                esta = True
                                break
                            else:
                                pass
                        if esta:
                            pass
                        else:

                            arrayFinal.append(array[num])
                            contFaciles+=1


            if array[num].dificultad == "Intermedio":

                if contMedio<medio:
                    if len(arrayFinal) == 0:
                        arrayFinal.append(array[num])
                    else:
                        esta = False
                        for k in arrayFinal:
                            if k.codigo == i.codigo:
                                esta = True
                                break
                            else:
                                pass
                        if esta:
                            pass
                        else:

                            arrayFinal.append(array[num])
                            contMedio += 1
            if array[num].dificultad == "Dificil":
               
                if contDificiles<dificil:
                    if len(arrayFinal) == 0:
                        arrayFinal.append(array[num])
                    else:
                        esta = False
                        for k in arrayFinal:
                            if k.codigo == i.codigo:
                                esta = True
                                break
                            else:
                                pass
                        if esta:
                            pass
                        else:

                            arrayFinal.append(array[num])
                            contDificiles += 1







def juego(playerGlobal):
    cargar_file()
    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')
    global arrayFinal,contFaciles,contMedio,contador,contPremio,contPremioSeguro,contDificiles
    arrayFinal.clear()
    contador=0
    contPremio=0
    contPremioSeguro=0
    contDificiles=0
    contMedio=0
    contFaciles=0



    lblJugador = Label(frame, text="Jugador:", font="Roman")
    lblJugador.place(relx=0.25, rely=0.05)

    lblJugador1 = Label(frame, text=playerGlobal.nombre + " " + playerGlobal.apellido, font="Roman")
    lblJugador1.place(relx=0.45, rely=0.05)

    lbl2=Label(frame,text="Elija la cantidad de preguntas", font="Roman 15")
    lbl2.place(relx=0.17, rely=0.25)

    lbl2 = Label(frame, text="                          ", font="Roman 16")
    lbl2.place(relx=0.47, rely=0.4)

    def mostrarPartidas():

        listaPartida = []
        for i in inventario.partidas:
            if i.cedula_player == playerGlobal.cedula:
                listaPartida.append(i)

        conta = len(listaPartida) - 1
        if len(listaPartida)<10:
            print("Ultimas Partidas")

            for i in listaPartida:
                print("                  ")
                print(conta+1)
                print(listaPartida[conta])
                conta -= 1
        else:
            print("Ultimas 10 Partidas")
            diez = 10
            for i in range(0,10):
                print("                  ")
                print(diez)
                diez-=1
                print(listaPartida[conta])
                conta-=1


    def cant1():
        text1=cant10['text']
        lbl2['text'] = text1

        cargarPreguntas(5,3,2)

    def cant2():
        text1=cant11['text']
        lbl2['text'] = text1
        cargarPreguntas(5, 4, 2)
    def cant3():
        text1=cant16['text']
        lbl2['text'] = text1
        cargarPreguntas(5, 5, 6)

    def continuar():
        cant = int(lbl2['text'])
        preguntas(playerGlobal,cant)
        frame.destroy()




    cant10=Button(frame, text="10", bg="blue", fg="white", font="Roman", command=cant1)
    cant10.place(relx=0.17, rely=0.6, relwidth=0.2, relheight=0.15)

    cant11 = Button(frame, text="11", bg="blue", fg="white", font="Roman", command=cant2)
    cant11.place(relx=0.40, rely=0.6, relwidth=0.2, relheight=0.15)

    cant16 = Button(frame, text="16", bg="blue", fg="white", font="Roman", command=cant3)
    cant16.place(relx=0.63, rely=0.6, relwidth=0.2, relheight=0.15)

    continuar = Button(frame, text="continuar", bg="blue", fg="white", font="Roman" ,command=continuar)
    continuar.place(relx=0.05, rely=0.8, relwidth=0.21, relheight=0.15)

    salir = Button(frame, text="salir", bg="blue", fg="white", font="Roman" ,command=frame.destroy)
    salir.place(relx=0.74, rely=0.8, relwidth=0.20, relheight=0.15)

    verPartidas = Button(frame, text="Ver mis partidas", bg="blue", fg="white", font="Roman", command=mostrarPartidas)
    verPartidas.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.15)




def iniciarSesion():
    cargar_file()
    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')








    lblCedula = Label(frame, text="Ingrese su cedula", font="Roman")
    lblCedula.pack(pady=10)

    txtCedula = Entry(frame, font="Roman")
    txtCedula.pack()

    lblContra = Label(frame, text="Ingrese su contraseña", font="Roman")
    lblContra.pack()

    txtContra = Entry(frame, font="Roman", show="*")
    txtContra.pack(pady=10)

    etiqueta2 = Label(frame)
    etiqueta2.pack()

    def buscar_objeto():
        cedula = txtCedula.get()
        password = txtContra.get()
        if len(list(inventario.buscar_player_cedula(cedula,password))) == 0:
            print("\nCedula o Contraseña incorrecta\n")
        else:

            hola = list(inventario.buscar_player_cedula(cedula,password))

            for g in hola:
                for file in os.listdir("./Files"):
                    if ''+g.cedula+'.json' in file:
                        playerGlobal = saver.load_json(file)


            juego(playerGlobal)
            frame.destroy()



    login = Button(frame, text="Login",bg="blue" ,fg="white", command= buscar_objeto)

    login.place(relx=0.25,rely=0.8, relwidth=0.20 , relheight=0.15)

    close = Button(frame, text="salir", bg="blue", fg="white", command=frame.destroy)
    close.place(relx=0.55, rely=0.8, relwidth=0.20, relheight=0.15)




def registrarse():

    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')

    lblCedula = Label(frame, text="Cedula:", font="Roman")
    lblCedula.place(relx=0.1, rely=0.05)


    txtCedula = Entry(frame, font="Roman")
    txtCedula.place(relx=0.40,rely=0.05)

    lblNombre = Label(frame, text="Nombre:", font="Roman")
    lblNombre.place(relx=0.1, rely=0.17)

    txtNombre = Entry(frame, font="Roman")
    txtNombre.place(relx=0.40, rely=0.17)

    lblApellido = Label(frame, text="Apellido:", font="Roman")
    lblApellido.place(relx=0.1, rely=0.29)

    txtApellido = Entry(frame, font="Roman")
    txtApellido.place(relx=0.40, rely=0.29)

    lblEdad = Label(frame, text="Edad:", font="Roman")
    lblEdad.place(relx=0.1, rely=0.41)

    txtEdad = Entry(frame, font="Roman")
    txtEdad.place(relx=0.40, rely=0.41)

    lblTelefono = Label(frame, text="Telefono:", font="Roman")
    lblTelefono.place(relx=0.1, rely=0.53)

    txtTelefono = Entry(frame, font="Roman")
    txtTelefono.place(relx=0.40, rely=0.53)

    lblDireccion = Label(frame, text="Direccion:", font="Roman")
    lblDireccion.place(relx=0.1, rely=0.65)

    txtDireccion = Entry(frame, font="Roman")
    txtDireccion.place(relx=0.40, rely=0.65)

    lblPassword = Label(frame, text="Contraseña:", font="Roman")
    lblPassword.place(relx=0.1, rely=0.77)

    txtPassword = Entry(frame, font="Roman")
    txtPassword.place(relx=0.40, rely=0.77)

    def guardarAyudante(playerGlobal):
        cargar_file()
        frame = Frame(ventana)

        frame.pack(expand=True, fill='both')
        lblText = Label(frame, text="Registrar Ayudante", font="Roman")
        lblText.place(relx=0.1, rely=0.01)

        lblCedula = Label(frame, text="Cedula:", font="Roman 12")
        lblCedula.place(relx=0.1, rely=0.115 , )

        txtCedula = Entry(frame, font="Roman 12")
        txtCedula.place(relx=0.40, rely=0.115)

        lblNombre = Label(frame, text="Nombre:", font="Roman 12")
        lblNombre.place(relx=0.1, rely=0.205)

        txtNombre = Entry(frame, font="Roman 12")
        txtNombre.place(relx=0.40, rely=0.205)

        lblApellido = Label(frame, text="Apellido:", font="Roman 12")
        lblApellido.place(relx=0.1, rely=0.295)

        txtApellido = Entry(frame, font="Roman 12")
        txtApellido.place(relx=0.40, rely=0.295)

        lblEdad = Label(frame, text="Edad:", font="Roman 12")
        lblEdad.place(relx=0.1, rely=0.385)

        txtEdad = Entry(frame, font="Roman 12")
        txtEdad.place(relx=0.40, rely=0.385)

        lblTelefono = Label(frame, text="Telefono:", font="Roman 12")
        lblTelefono.place(relx=0.1, rely=0.475)

        txtTelefono = Entry(frame, font="Roman 12")
        txtTelefono.place(relx=0.40, rely=0.475)

        lblDireccion = Label(frame, text="Direccion:", font="Roman 12")
        lblDireccion.place(relx=0.1, rely=0.565)

        txtDireccion = Entry(frame, font="Roman 12")
        txtDireccion.place(relx=0.40, rely=0.565)

        lblCategoria = Label(frame, text="Categoria:", font="Roman 12")
        lblCategoria.place(relx=0.1, rely=0.655)

        cbCategoria = tkinter.ttk.Combobox(frame, font="Roman 12",state="readonly")
        cbCategoria.place(relx=0.40, rely=0.655 , relwidth = 0.51 )
        cbCategoria['values'] = ('Seleccionar')
        cbCategoria.current(0)

        def loadAyudante():
            cedulaP= playerGlobal.cedula
            print(cedulaP)
            value = cbCategoria.get()
            if txtCedula.get() == "" or txtNombre.get() == "" or txtApellido.get() == "" or txtEdad.get() == "" or txtTelefono.get() == "" or txtDireccion.get() == "" or value == "Seleccionar":
                print("No pueden haber campos vacios")
            else:


                categoria = 0

                for i in inventario.categorias:
                    if value == i.categoria:
                        categoria=i.codigo

                ayudante = Ayudante(txtCedula.get(), txtNombre.get(), txtApellido.get(), float(txtEdad.get()),
                                txtTelefono.get(), txtDireccion.get(), categoria,cedulaP)
                print("Guardado con exito")

                cbCategoria.current(0)
                saver.save_json(ayudante)

        btnGuardar = Button(frame, text="Guardar", bg="blue", fg="white", font="Roman", command=loadAyudante)
        btnGuardar.place(relx=0.1, rely=0.8, relwidth=0.30, relheight=0.1)

        def abrirJuego():
            juego(playerGlobal)
            frame.destroy()
        close = Button(frame, text="cerrar", bg="blue", fg="white", font="Roman", command=abrirJuego)
        close.place(relx=0.55, rely=0.8, relwidth=0.30, relheight=0.1)

        lista = inventario.categorias




        for i in lista:
            values = list(cbCategoria["values"])

            valor = i.categoria
            cbCategoria["values"] = values + [valor]





    def guardar():
        if txtCedula.get() == "" or txtNombre.get() == "" or txtApellido.get() == "" or txtEdad.get() == "" or txtTelefono.get() == "" or txtDireccion.get() == "" or txtPassword.get() == "":
            print("No pueden haber campos vacios")
        else:
            player = Player(txtCedula.get(),txtNombre.get(),txtApellido.get(),float(txtEdad.get()),txtTelefono.get(),txtDireccion.get(),txtPassword.get())
            saver.guardar_bd(player)
            saver.save_json(player)
            print("Guardado con exito")
            playerGlobal = player
            guardarAyudante(playerGlobal)
            frame.destroy()


    btnGuardar = Button(frame, text="Guardar", bg="blue", fg="white", font="Roman", command=guardar)
    btnGuardar.place(relx=0.1, rely=0.90, relwidth=0.30, relheight=0.1)

    close = Button(frame, text="close", bg="blue", fg="white",font="Roman", command=frame.destroy)
    close.place(relx=0.55, rely=0.90, relwidth=0.30, relheight=0.1)



btnIniciarSesion=Button(ventana,text = "Iniciar Sesion",bg="blue",fg="white" , font="Roman",command = iniciarSesion )
btnIniciarSesion.place(relx=0.3,rely = 0.3,relwidth=0.40, relheight=0.15)




btnRegistrarse=Button(ventana,text = "Registrarse",bg="blue" ,fg="white", font="Roman",command = registrarse)
btnRegistrarse.place(relx=0.3,rely = 0.5, relwidth=0.40, relheight=0.15)






ventana.mainloop()




if __name__ == '__main__':
    saver = Persistencia()
    saver.connect()
    inventario = Inventario()
    cargar_file()








