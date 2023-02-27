def seq3np1(n):
    """
    Print the 3n + 1 sequence from n, terminating when it reaches 1.
    Imprima a sequência 3n+1 de n, terminando quando atingir 1.
    """

    cont = 0
    while n != 1:
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        cont += 1
    print('O codigo tever ', cont, ' interacoes.')

for start in range(1, 51):
    print('Para ', start, ' temos')
    seq3np1(start)
