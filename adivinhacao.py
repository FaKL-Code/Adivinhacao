from random import randint

print("Este é um jogo de adivinhação")
print("-----------------------------")

numero = randint(0, 100)

tentativas = 5

rodada = 1

while tentativas > 0:
    
    print("tentativa {} de {}".format(rodada, tentativas))

    valor_inserido = int(input("Digite o número: "))

    acertou = valor_inserido == numero

    maior = valor_inserido > numero

    menor = valor_inserido < numero

    print("Você digitou: ", valor_inserido)

    if acertou:
        print("Você acertou")
    else:

        if maior:
            print("O número é menor que isso")

        elif menor:
            print("O número é maior")
            
        rodada += 1
    
    if rodada > tentativas:
        break
    
print("O número era: ", numero)
