class Player:



    def __init__(self,cedula,nombre,apellido,edad,telefono,direccion,password,*args):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.password = password



    def __str__(self):
        return f"{self.cedula}--{self.nombre}--{self.apellido}--{self.edad}--{self.telefono}--{self.direccion}--{self.password}"

    def __repr__(self):
        return f"\nCedula: {self.cedula}\nNombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}" \
               f"\nTelefono: {self.telefono}\nDireccion: {self.direccion}\nContraseña: {self.password}\n"





