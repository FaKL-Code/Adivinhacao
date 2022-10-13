from random import randint

print("Este é um jogo de adivinhação")
print("-----------------------------")

numero = randint(0, 100)

tentativas = 5

rodada = 1

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

        elif menor:
            print("O número é maior")
    
print("O número era: ", numero)
