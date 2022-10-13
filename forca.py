
from random import randint
import titulos

def start():
    
    titulos.titulo(2)
    palavra = escolher_palavra()
    letras_certas = letras_acertadas(palavra)
    
    enforcou = False
    acertou = False
    erros = 0
            
    print(letras_certas)

    while not enforcou and not acertou:
        print("Jogando!")
        
        palpite = str(input("Escolha uma letra: ")).upper()
        
        if(palpite in palavra):
            valida_chute(palavra, palpite, letras_certas)
        else: 
            erros += 1
            
        enforcou = erros == 6
        acertou = "_" not in letras_certas
            
        print(letras_certas)
        
    if acertou:
        vitoria()
    else:
        derrota()
        print("A palavra era: ", palavra)

def escolher_palavra():
    
    file = open("palavra.txt", "r")
    
    palavras = []
    
    for linha in file:
        linha.strip
        palavras.append(linha)
        
    palavra = str(palavras[randint(0, len(palavras) - 1)]).upper().strip()     
    
    file.close()
    
    return palavra

def letras_acertadas(palavra):
    lista = ["_" for letra in palavra]
    return lista

def valida_chute(palavra, palpite, letras_certas):
    pos = 0
    for letra in palavra:
        if(palpite == letra):
            letras_certas[pos] = letra
        pos += 1
        
def vitoria():
    print("Você ganhou!")
    
def derrota():
    print("Você perdeu!")

if (__name__ == "__main__"):
    start()