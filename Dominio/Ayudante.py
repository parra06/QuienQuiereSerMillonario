class Ayudante:



    def __init__(self,cedula,nombre,apellido,edad,telefono,direccion,categoria,cedula_player,*args):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.categoria = categoria
        self.cedula_player = cedula_player



    def __str__(self):
        return f"{self.cedula}--{self.nombre}--{self.apellido}--{self.edad}--{self.telefono}--{self.direccion}--{self.categoria}--{self.cedula_player}"

    def __repr__(self):
        return f"\nCedula: {self.cedula}\nNombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}" \
               f"\nTelefono: {self.telefono}\nDireccion: {self.direccion}\nContraseña: {self.password}\n"





