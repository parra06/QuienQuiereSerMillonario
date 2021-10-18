from Dominio.Player import Player
from Dominio.Categoria import Categoria
from Dominio.Pregunta import Pregunta
from Dominio.Partida import Partida
from Dominio.Ayudante import Ayudante


class Inventario():

    def __init__(self):
        self.players = []
        self.categorias = []
        self.preguntas = []
        self.partidas = []
        self.ayudantes = []

    def eliminar_listas(self):
        self.players.clear()
        self.categorias.clear()
        self.preguntas.clear()
        self.partidas.clear()
        self.ayudantes.clear()




    def agregar_objeto(self, objeto):


        if type(objeto) == Player:

            if len(list(self.buscar_player_cedula(objeto.cedula,objeto.password))) == 0:
                self.players.append(objeto)


            else:
                print('Player repetido')
                raise Exception('Player repetido')

        if type(objeto) == Categoria:
            if len(list(self.buscar_categoria_codigo(objeto.codigo))) == 0:
                self.categorias.append(objeto)


            else:
                print('Categoria repetida')
                raise Exception('Categoria repetida')

        if type(objeto) == Pregunta:
            if len(list(self.buscar_pregunta_codigo(objeto.codigo))) == 0:
                self.preguntas.append(objeto)


            else:
                print('Pregunta repetida')
                raise Exception('Pregunta repetida')

        if type(objeto) == Partida:

            self.partidas.append(objeto)


        if type(objeto) == Ayudante:
            if len(list(self.buscar_ayudante_cedula(objeto.cedula))) == 0:
                self.ayudantes.append(objeto)


            else:
                print('Ayudante repetido')
                raise Exception('Ayudante repetido')


    # ------------------------------------------------------

    def buscar_player_cedula(self,cedula,password):

        for g in self.players:
            if g.cedula == cedula and g.password == password:
                yield g

    def buscar_ayudante_cedula(self,cedula):

        for g in self.ayudantes:
            if g.cedula == cedula:
                yield g

    def buscar_categoria_codigo(self,codigo):

        for g in self.categorias:
            if g.codigo == codigo:
                yield g

    def buscar_pregunta_codigo(self,codigo):

        for g in self.preguntas:
            if g.codigo == str(codigo):
                yield g

    def buscar_partida_id(self,id):

        for g in self.partidas:
            if g.id == id:
                yield g

    def buscar_partida_cedula(self,cedula):
        for g in self.partidas:
            if g.cedula_player == cedula:
                yield g







