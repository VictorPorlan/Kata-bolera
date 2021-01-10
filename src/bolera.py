class Bolera:
    resultado = 0
    pleno = 10
    fallo = 0
    max_turnos = 10

    def __init__(self,puntos):
        self.puntos = list(puntos)
    
    def recorrer_lista(self):
        for numero in self.puntos:
            Bolera.resultado = Bolera.resultado + int(numero)
        return Bolera.resultado
    



