# Exercícios
# Ex2 e Ex3: Definição de hora.

class Hora:

# AM: Ante Meridiem (antes do meio-dia)
# PM: Post Meridiem (depois do meio-dia)

    def __init__(self, hora = 0, minutos = 0, segundos = 0):

        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos

    def alarme(self, tempo):

        self.segundos, tempo.minutos = (self.segundos + tempo.segundos) % 60, (self.segundos + tempo.segundos) // 60
        self.minutos, tempo.hora = (self.minutos + tempo.minutos) % 60, (self.minutos + tempo.minutos) // 60
        self.hora = (self.hora + tempo.hora) % 24

    def __str__(self):

        return str(self.hora) + "h " + str(self.minutos) + "min " + str(self.segundos) + "seg"

def main ():

    hora = Hora
    hora.hora = int(input("Digite a hora: "))
    hora.minutos = int(input("Digite os minutos: "))
    hora.segundos = int(input("Digite os segundos: "))
    assert (hora.hora < 24 and hora.minutos < 60 and hora.segundos <60) and (hora.hora >= 0 and hora.minutos >= 0 and hora.segundos >= 0)

    tempo_alarme = Hora
    tempo_alarme.hora = int(input("Digite o tempo do alarme: "))

    hora.alarme(tempo_alarme)
    print (hora)

main ()

# Escrever testes
