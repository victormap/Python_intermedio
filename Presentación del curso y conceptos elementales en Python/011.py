class Persona():
    def __init__(self):
        pass

    def despedir(self):
        print("Adiós")

    @classmethod
    def saludar(cls,nombre):
        print("Estoy saludando"+nombre)

Persona.saludar("Juan")