from random import randint

def start():

    print("Este é um jogo de adivinhação")
    print("-----------------------------")

    numero = randint(0, 100)

    rodada = 1

    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("1- Fácil  2- Médio  3- Difícil")

    dificuldade = int(input(""))

    if dificuldade == 1:
        tentativas = 10
        
    elif dificuldade == 2:
        tentativas = 7
        
    elif dificuldade == 3:
        tentativas = 5

    for rodada in range (1, tentativas + 1):
        
        print("tentativa {} de {}".format(rodada, tentativas))

        valor_inserido = int(input("Digite um número entre 1 e 100: "))
        
        print("Você digitou: ", valor_inserido)
        
        if valor_inserido < 1 or valor_inserido > 100:
            print("Número invalido")
            continue

        acertou = valor_inserido == numero

        maior = valor_inserido > numero

        menor = valor_inserido < numero

        if acertou:
            print("Você acertou")
            break
        
        else:

            if maior:
                print("O número é menor que isso")
                pontos = pontos - (valor_inserido - numero)

            elif menor:
                print("O número é maior")
                pontos = pontos - (numero - valor_inserido)
        
    print("O número era: ", numero)
    print("Você pontuou: {} pontos".format(pontos))

if (__name__ == "__main__"):
    start()