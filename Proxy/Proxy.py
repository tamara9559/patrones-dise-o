
from abc import ABC, abstractmethod

# Interfaz común
class Documento(ABC):
    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def editar(self, nuevo_contenido):
        pass

# Documento real
class DocumentoReal(Documento):
    def __init__(self, contenido):
        self.contenido = contenido

    def mostrar(self):
        print("Contenido del documento:", self.contenido)

    def editar(self, nuevo_contenido):
        self.contenido = nuevo_contenido
        print("Documento editado correctamente.")

# Proxy con control de acceso y permisos
class DocumentoProxy(Documento):
    def __init__(self, contenido, contraseña, permiso_edicion=False):
        self.documento_real = DocumentoReal(contenido)
        self.contraseña = contraseña
        self.permiso_edicion = permiso_edicion

    def mostrar(self):
        if self.verificar_acceso():
            self.documento_real.mostrar()
        else:
            print("¡Acceso denegado! Contraseña incorrecta.")

    def editar(self, nuevo_contenido):
        if not self.verificar_acceso():
            print("¡Acceso denegado! Contraseña incorrecta.")
            return
        if self.permiso_edicion:
            self.documento_real.editar(nuevo_contenido)
        else:
            print("¡Permiso denegado! Solo tienes acceso de lectura.")

    def verificar_acceso(self):
        intento = input("Ingrese la contraseña para acceder al documento: ")
        return intento == self.contraseña

# Uso
if __name__ == "__main__":
    # Caso con solo lectura
    doc_lectura = DocumentoProxy("Documento solo lectura.", "1234", permiso_edicion=False)
    doc_lectura.mostrar()
    doc_lectura.editar("Intento de editar contenido.")

    print()

    # Caso con permisos de edición
    doc_edicion = DocumentoProxy("Documento editable.", "5678", permiso_edicion=True)
    doc_edicion.mostrar()
    doc_edicion.editar("Nuevo contenido del documento.")
    doc_edicion.mostrar()
