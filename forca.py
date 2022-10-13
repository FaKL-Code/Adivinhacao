
def start():

    print("*********************************")
    print("******* Jogo da Forca! *******")
    print("*********************************")

    palavra = "banana"
    
    enforcou = False
    
    acertou = False
    
    while not enforcou and not acertou:
        print("Jogando!")
        
        palpite = input("Escolha uma letra: ").strip
        
        pos = 0
        
        for letra in palavra:
            if(palpite == letra):
                print("Temos a letra {} na posição {}!".format(letra, pos))
            pos += 1
        
    print("Fim do jogo!")
    
if (__name__ == "__main__"):
    start()