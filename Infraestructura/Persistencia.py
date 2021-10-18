
import sqlite3
import jsonpickle

from Dominio.Player import Player
from Dominio.Categoria import Categoria
from Dominio.Pregunta import Pregunta
from Dominio.Partida import Partida
from Dominio.Ayudante import Ayudante


class Persistencia():

    def connect(self):
        self.con = sqlite3.connect("qqsm.db")
        self.__crear_tabla_player()
        self.__crear_tabla_categoria()
        self.__crear_tabla_pregunta()



    def __crear_tabla_player(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PLAYER(cedula text primary key,nombre text, apellido text," \
                    " edad float, telefono text, direccion text, password text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def __crear_tabla_categoria(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE CATEGORIA(codigo float primary key,categoria text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def __crear_tabla_pregunta(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PREGUNTA(codigo float primary key,pregunta text, opcion_a text," \
                    " opcion_b text, opcion_c text, opcion_d text, respuesta text,cod_categoria float,dificultad text, valor float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass




    def guardar_bd(self,objeto):
        cursor = self.con.cursor()



        if isinstance(objeto,Player):
            query = "insert into PLAYER(cedula ,nombre, apellido ," \
                    "edad,telefono,direccion,password ) values(" \
                    f" ?,?,?,?,?,?,?)"
            cursor.execute(query, (str(objeto.cedula), objeto.nombre, objeto.apellido,
                                   objeto.edad, objeto.telefono, objeto.direccion,objeto.password))

        elif isinstance(objeto,Categoria):
            query = "insert into CATEGORIA(codigo ,categoria) values(" \
                    f" ?,?)"
            cursor.execute(query, (str(objeto.codigo), objeto.categoria))

        else:
            query = "insert into PREGUNTA(codigo ,pregunta, opcion_a ," \
                    "opcion_b,opcion_c,opcion_d,respuesta,cod_categoria, dificultad ,valor ) values(" \
                    f" ?,?,?,?,?,?,?,?,?,?)"
            cursor.execute(query, (str(objeto.codigo), objeto.pregunta, objeto.opcion_a,
                                   objeto.opcion_b, objeto.opcion_c, objeto.opcion_d, objeto.respuesta,
                                   objeto.cod_categoria,objeto.dificultad,objeto.valor))




        self.con.commit()



    @classmethod
    def save_json(cls, objeto):

        if isinstance(objeto,Player):
            text_open = open("Files/" + str(objeto.cedula) + '.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()

        if isinstance(objeto,Categoria):
            text_open = open("Files/" + str(objeto.codigo) +"_"+str(objeto.categoria) +'.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()

        if isinstance(objeto,Pregunta):
            text_open = open("Files/" + str(objeto.codigo)+'.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()

        if isinstance(objeto,Partida):
            text_open = open("Files/" + str(objeto.id)+'.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()

        if isinstance(objeto,Ayudante):
            text_open = open("Files/" + str(objeto.cedula)+'A.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()




    @classmethod
    def load_json(cls, file_name):
        text_open = open("Files/" + file_name, mode='r')
        json_gui = text_open.readline()
        objeto = jsonpickle.decode(json_gui)
        text_open.close()
        return objeto

    def load_json_config(self,file_name):
        text_open = open("config/" + file_name, mode='r')
        json_gui = text_open.readline()
        objeto = jsonpickle.decode(json_gui)
        text_open.close()
        return objeto