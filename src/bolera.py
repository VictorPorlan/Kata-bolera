class Bolera:
    resultado = 0
    pleno = 10
    fallo = 0
    
    def __init__(self,puntos):
        self.puntos = list(puntos)
    
    def divisor_turnos(self):
        lista = []
        partida = []
        turnos = 0
        for numero in self.puntos:
            lista.append(numero)
            if 'X' in lista and turnos == 9 and len(lista) == 3:
                partida.append(lista)
                lista = []
            if '/' in lista and turnos == 9 and len(lista) == 3:
                partida.append(lista)
                lista = []
            if 'X' not in lista and "/" not in lista and turnos == 9 and len(lista) == 2:
                partida.append(lista)
                lista = []
            if len(lista) == 2 and turnos != 9:
                partida.append(lista)
                lista = []
                turnos += 1
            elif "X" in lista and turnos != 9:
                partida.append(lista)
                lista = []
                turnos += 1
        return partida

    def recorrer_lista(self):
        for numero in self.puntos:
            Bolera.resultado = Bolera.resultado + int(numero)
        return Bolera.resultado
print (Bolera("XXXXXXXXXXXX").divisor_turnos())
