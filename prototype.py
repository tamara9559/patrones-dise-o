import copy

class Enemigo:
    def clonar(self):
        return copy.deepcopy(self)


class Zombi(Enemigo):
    def __init__(self, vida, dano, velocidad, habilidades=None):
        self.vida = vida
        self.dano = dano
        self.velocidad = velocidad
        self.habilidades = habilidades if habilidades is not None else []

    def __str__(self):
        return f"Zombi {{vida={self.vida}, dano={self.dano}, velocidad={self.velocidad}, habilidades={self.habilidades}}}"


def juego():
    zombi_base = Zombi(100, 10, 1.5)

    zombi1 = zombi_base.clonar()
    zombi2 = zombi_base.clonar()
    zombi3 = zombi_base.clonar()

    zombi1.vida = 120
    zombi2.velocidad = 2.0
    zombi3.habilidades.append("vomitar ácido")

    print("Zombi base:", zombi_base)
    print("Zombi 1:", zombi1)
    print("Zombi 2:", zombi2)
    print("Zombi 3:", zombi3)


juego()
