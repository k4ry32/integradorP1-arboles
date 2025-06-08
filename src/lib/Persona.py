class Persona:
    def __init__(self, apellido, nombre, dni):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        # Muestra apellido, nombre y DNI de la persona
        return f"{self.apellido} {self.nombre}, DNI: {self.dni}"