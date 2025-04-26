# bridge.py

class Dispositivo:
    def __init__(self, implementacion):
        self.implementacion = implementacion

    def encender(self):
        self.implementacion.encender()

    def apagar(self):
        self.implementacion.apagar()

    def establecer_canal(self, canal):
        if hasattr(self.implementacion, "establecer_canal"):
            self.implementacion.establecer_canal(canal)
        else:
            print("Este dispositivo no soporta establecer canal.")

    def agregar_cd(self, cd):
        if hasattr(self.implementacion, "agregar_cd"):
            self.implementacion.agregar_cd(cd)
        else:
            print("Este dispositivo no soporta agregar CD.")

class TVImplementacion:
    def encender(self):
        print("TV: Encendiendo")

    def apagar(self):
        print("TV: Apagando")

    def establecer_canal(self, canal):
        print(f"TV: Estableciendo canal en {canal}")

class RadioImplementacion:
    def encender(self):
        print("Radio: Encendiendo")

    def apagar(self):
        print("Radio: Apagando")

    def establecer_canal(self, canal):
        print(f"Radio: Sintonizando estación {canal}")

class DVDImplementacion:
    def encender(self):
        print("DVD: Encendiendo")

    def apagar(self):
        print("DVD: Apagando")

    def agregar_cd(self, cd):
        print(f"DVD: Insertando el CD '{cd}'")

# Uso
tv = Dispositivo(TVImplementacion())
radio = Dispositivo(RadioImplementacion())
dvd = Dispositivo(DVDImplementacion())

tv.encender()
tv.establecer_canal(5)
tv.apagar()

radio.encender()
radio.establecer_canal("98.5 FM")
radio.apagar()

dvd.encender()
dvd.agregar_cd("Película Matrix")
dvd.apagar()
