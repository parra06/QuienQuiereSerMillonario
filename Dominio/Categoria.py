class Categoria:

    def __init__(self,codigo,categoria):
        self.codigo = codigo
        self.categoria = categoria

    def __str__(self):
        return f"{self.codigo}--{self.categoria}"

    def __repr__(self):
        return f"\nCodigo: {self.codigo}\nCategoria: {self.categoria}\n"