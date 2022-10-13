from random import randint

print("Este é um jogo de adivinhação")
print("-----------------------------")

numero = randint(0, 100)

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
    
    print("Você errou")
    
print("O número era: ", numero)
