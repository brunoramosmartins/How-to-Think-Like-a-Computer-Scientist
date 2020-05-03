# Você terá umas férias maravilhosas que começam no dia 3, quarta-feira.
# você retornará das suas férias depois de 137 noites (Uauu!). Escreva
# um programa que pede o dia do mês e o dia da semana em que você irá
# viajar e pede ainda o número de dias que você ficará de férias e
# imprima o dia da semana que você voltará.

def main ():

    dia_mes = int(input("Digite o dia que inicia suas férias: "))

    semana = [
            "segunda-feira",
            "terça-fera",
            "quarta-feira",
            "quinta-feira",
            "sexta-feira",
            "sábado",
            "domingo"
            ]
    dia_semana = input("Qual dia da semana começa suas férias? ")
    while dia_semana.lower() not in semana:
        print("Desculpe, escreva o dia corretamente.")
        print("Ex: segunda-feria")
        dia_semana = input("Qual dia da semana começa suas férias? ")

    dias_ferias = int(input("Quantos dias você ficará de férias? "))
