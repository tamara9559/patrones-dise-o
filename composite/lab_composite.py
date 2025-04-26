import os
from abc import ABC, abstractmethod

# Componente base
class ArchivoComponent(ABC):

    @abstractmethod
    def get_nombre(self):
        pass

    @abstractmethod
    def get_tamaño(self):
        pass

    @abstractmethod
    def mostrar(self, indentacion):
        pass

    @abstractmethod
    def crear_en_sistema(self, ruta_base):
        pass


# Hoja: Archivo individual
class Archivo(ArchivoComponent):
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño

    def get_nombre(self):
        return self.nombre

    def get_tamaño(self):
        return self.tamaño

    def mostrar(self, indentacion):
        print(f"{indentacion}📄 Archivo: {self.nombre} ({self.tamaño} bytes)")

    def crear_en_sistema(self, ruta_base):
        ruta_completa = os.path.join(ruta_base, self.nombre)
        with open(ruta_completa, 'w') as f:
            f.write("Contenido simulado del archivo.\n")
        print(f"✅ Archivo creado: {ruta_completa}")


# Compuesto: Carpeta
class Carpeta(ArchivoComponent):
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def get_nombre(self):
        return self.nombre

    def get_tamaño(self):
        tamaño_total = sum(componente.get_tamaño() for componente in self.hijos)
        return tamaño_total

    def añadir(self, componente):
        self.hijos.append(componente)

    def eliminar(self, componente):
        self.hijos.remove(componente)

    def mostrar(self, indentacion):
        print(f"{indentacion}📁 Carpeta: {self.nombre} ({self.get_tamaño()} bytes)")
        for componente in self.hijos:
            componente.mostrar(indentacion + "    ")

    def crear_en_sistema(self, ruta_base):
        ruta_actual = os.path.join(ruta_base, self.nombre)
        os.makedirs(ruta_actual, exist_ok=True)
        print(f"📁 Carpeta creada: {ruta_actual}")
        for componente in self.hijos:
            componente.crear_en_sistema(ruta_actual)


# Cliente
if __name__ == "__main__":
    # Crear estructura lógica
    raiz = Carpeta("Raíz")

    documentos = Carpeta("Documentos")
    imagenes = Carpeta("Imágenes")
    proyectos = Carpeta("Proyectos")

    archivo1 = Archivo("documento.txt", 100)
    archivo2 = Archivo("foto.jpg", 2000)
    archivo3 = Archivo("config.xml", 300)
    archivo4 = Archivo("main.py", 150)
    archivo5 = Archivo("README.md", 50)

    documentos.añadir(archivo1)
    documentos.añadir(archivo3)
    imagenes.añadir(archivo2)
    proyectos.añadir(archivo4)
    proyectos.añadir(archivo5)
    documentos.añadir(proyectos)

    raiz.añadir(documentos)
    raiz.añadir(imagenes)

    # Mostrar estructura lógica
    print("📂 Estructura del Archivador:")
    raiz.mostrar("")

    print(f"\n📦 Tamaño total: {raiz.get_tamaño()} bytes")

    # Crear en sistema de archivos
    print("\n📁 Creando estructura en el sistema de archivos...")
    ruta_destino = os.path.join(os.getcwd(), "estructura_archivador")
    raiz.crear_en_sistema(ruta_destino)
    print(f"\n✅ Estructura creada en: {ruta_destino}")


