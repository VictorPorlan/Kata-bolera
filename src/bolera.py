class Bolera:

    def __init__(self,puntos):
        self.puntos = list(puntos)

    def recorrer_lista(self):
        turnos = 0
        resultado = 0
        pleno = 10
        acumulador_pleno = 0
        acumulador_pleno_2 = 0
        acumulador_spare = 0
        ultimo_numero = 0
        tiradas_en_el_turno = 0
        for numero in self.puntos:
            valor = 0
            if numero.isdigit() and turnos == 9:
                valor += int(numero)
                if acumulador_pleno > 0:
                    valor += int(numero)
                    acumulador_pleno -= 1
                if acumulador_pleno_2 > 0:
                    valor += int(numero)
                    acumulador_pleno_2 -= 1
                if acumulador_spare == 1:
                    valor += int(numero)
                    acumulador_spare -= 1
                resultado += valor
                ultimo_numero = int(numero)
            if numero == "X" and turnos == 9:
                valor += pleno
                if acumulador_pleno > 0:
                    valor += pleno
                    acumulador_pleno -= 1
                if acumulador_pleno_2 > 0:
                    valor += pleno
                    acumulador_pleno_2 -= 1
                if acumulador_spare == 1:
                    valor += pleno
                    acumulador_spare -= 1
                resultado += valor
            if numero == "-" and turnos == 9:
                if acumulador_pleno > 0:
                    acumulador_pleno -= 1
                if acumulador_pleno_2 > 0:
                    acumulador_pleno_2 -= 1
                if acumulador_spare >= 0:
                    acumulador_spare = 0
                ultimo_numero = 0
            if numero == "/" and turnos == 9:
                valor = 10 - ultimo_numero
                if acumulador_pleno > 0:
                    valor = 10 - ultimo_numero
                    acumulador_pleno -= 1
                resultado += valor
            if numero == "X" and turnos != 9:
                valor += pleno
                if acumulador_pleno > 0:
                    valor += pleno
                    acumulador_pleno -= 1
                if acumulador_pleno_2 > 0:
                    valor += pleno
                    acumulador_pleno_2 -= 1
                if acumulador_spare == 1:
                    valor += pleno
                    acumulador_spare -= 1
                if acumulador_pleno == 0:
                    acumulador_pleno = 2
                else:
                    acumulador_pleno_2 = 2
                resultado += valor
                valor = 0
                tiradas_en_el_turno = 0
                turnos += 1
            if numero == "/" and turnos != 9:
                valor = 10 - ultimo_numero
                acumulador_spare += 1
                if acumulador_pleno > 0:
                    valor += 10 - ultimo_numero
                    acumulador_pleno -= 1
                if acumulador_pleno_2 > 0:
                    valor += 10 - ultimo_numero
                    acumulador_pleno_2 -= 1
                tiradas_en_el_turno = 0
                turnos += 1
                resultado += valor
                valor = 0
            if numero == "-" and turnos != 9:
                if acumulador_pleno > 0:
                    acumulador_pleno -= 1
                if acumulador_pleno_2 > 0:
                    acumulador_pleno_2 -= 1
                if acumulador_spare >= 0:
                    acumulador_spare = 0
                tiradas_en_el_turno += 1
                if tiradas_en_el_turno == 2:
                    tiradas_en_el_turno = 0
                    turnos += 1
                ultimo_numero = 0
                valor = 0
            if numero.isdigit() and turnos != 9:
                valor += int(numero)
                if acumulador_pleno > 0:
                    valor += int(numero)
                    acumulador_pleno -= 1
                if acumulador_pleno_2 > 0:
                    valor += int(numero)
                    acumulador_pleno_2 -= 1
                if acumulador_spare == 1:
                    valor += int(numero)
                    acumulador_spare -= 1
                tiradas_en_el_turno += 1
                if tiradas_en_el_turno == 2:
                    tiradas_en_el_turno = 0
                    turnos += 1
                resultado += valor
                ultimo_numero = int(numero)
                valor = 0
        return resultado

