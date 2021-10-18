import uuid


class Partida:



    def __init__(self,cedula_player,premio,cant_respuestas_buenas,*args):
        self.id = str(uuid.uuid4())
        self.cedula_player = cedula_player
        self.premio = premio
        self.cant_respuestas_buenas = cant_respuestas_buenas




    def __str__(self):
        return f"Id: {self.id}\nCedula Player: {self.cedula_player}\nPremio: {self.premio}\nCantidad Respuestas Buenas: {self.cant_respuestas_buenas}\n"







