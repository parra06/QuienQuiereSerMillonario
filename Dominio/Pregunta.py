class Pregunta:

    def __init__(self,codigo,pregunta,opcion_a,opcion_b,opcion_c,opcion_d,respuesta,cod_categoria,dificultad,valor):
        self.codigo = codigo
        self.pregunta = pregunta
        self.opcion_a = opcion_a
        self.opcion_b = opcion_b
        self.opcion_c = opcion_c
        self.opcion_d = opcion_d
        self.respuesta = respuesta
        self.cod_categoria = cod_categoria
        self.dificultad = dificultad
        self.valor = valor

    def __str__(self):
        return f"{self.codigo}--{self.pregunta}--{self.opcion_a}--{self.opcion_b}--{self.opcion_c}--{self.opcion_d}--{self.respuesta}--{self.cod_categoria}--{self.dificultad}--{self.valor}"

    def __repr__(self):
        return f"\nCodigo: {self.codigo}\nPregunta: {self.pregunta}\nOpcion A: {self.opcion_a}\nOpcion B: {self.opcion_b}\nOpcion C: {self.opcion_c}\nOpcion D: {self.opcion_d}\nRespuesta: {self.respuesta}\nCodigo Categoria: {self.cod_categoria}\nDificultad: {self.dificultad}\nValor: {self.valor}\n"