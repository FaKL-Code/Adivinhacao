
def start():

    print("*********************************")
    print("******* Jogo da Forca! *******")
    print("*********************************")

    palavra = "banana".upper()
    
    letras_certas = ["_" for letra in palavra]
    
    enforcou = False
    
    acertou = False
    
    erros = 0
    
    print(letras_certas)

    while not enforcou and not acertou:
        print("Jogando!")
        
        palpite = input("Escolha uma letra: ").strip.upper()
        
        pos = 0
        
        if(palpite in palavra):
            for letra in palavra:
                if(palpite == letra):
                    letras_certas[pos] = letra
                pos += 1
        else: 
            erros += 1
            
        enforcou = erros == 6
        
        acertou = "_" not in letras_certas
            
        print(letras_certas)
        
    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
        
        
    print("Fim do jogo!")
    
if (__name__ == "__main__"):
    start()