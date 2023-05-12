from abc import ABC, abstractmethod

class Estaciones(ABC):
    def __init__(self, nombre, temperatura_media):
        self.nombre = nombre
        self.temperatura_media = temperatura_media

    @abstractmethod
    def descripcion(self):
        pass

class Primavera(Estaciones):
    def __init__(self, nombre, temperatura_media, flores):
        super().__init__(nombre, temperatura_media)
        self.flores = flores

    def descripcion(self):
        return f"La {self.nombre} es una estación con una temperatura media de {self.temperatura_media} grados y en la que florecen {self.flores}"

class Verano(Estaciones):
    def __init__(self, nombre, temperatura_media, actividades):
        super().__init__(nombre, temperatura_media)
        self.actividades = actividades

    def descripcion(self):
        return f"El {self.nombre} es una estación con una temperatura media de {self.temperatura_media} grados y en el que se realizan actividades como {self.actividades}"

class Otoño(Estaciones):
    def __init__(self, nombre, temperatura_media, colores):
        super().__init__(nombre, temperatura_media)
        self.colores = colores

    def descripcion(self):
        return f"El {self.nombre} es una estación con una temperatura media de {self.temperatura_media} grados y en el que predominan los colores {self.colores}"