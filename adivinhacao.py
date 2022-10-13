from random import randint

print("Este e um jogo de adivinhacao")
print("-----------------------------")

numero = randint(0, 100)

valor_inserido = int(input("Digite o numero: "))

print("Voce digitou: ", valor_inserido)

if(valor_inserido == numero):
    print("Voce acertou")
else:
    print("Voce errou")
    
print("O numero era: ", numero)
