from claseOrco import Orco


class Humano():

    def __init__(self, nombre, armadura, nivel, ataque, ojos=2, piernas=2, dientes=32, salud=100):
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = salud


    def atacar(self, orco):
        vida_Orco = Orco(self.salud) - self.ataque + Orco(self.armadura)
        print(vida_Orco)

    def no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def atributos_actual(self):
        print("Nombre: ", self.nombre, " | ", "Armadura: ", self.armadura, " | ", "Nivel: ", self.nivel, " | ", "Ataque: ", self.ataque, " | ", "Ojos: ", self.ojos, " | ", "Piernas: ", self.piernas, " | ", "Dientes: ", self.dientes, " | ", "Salud: ", self.salud, " | ",)


