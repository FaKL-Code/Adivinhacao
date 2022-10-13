import forca
import adivinhacao

def main():

    print("*********************************")
    print("******* Escolha o seu jogo! *******")
    print("*********************************")

    print("1- Forca 2- Adivinhação")

    jogo = int(input(""))

    if jogo == 1:
        print("Jogando Forca")
        forca.start()
    elif jogo == 2:
        print("Jogando Adivinhação")
        adivinhacao.start()
    else:
        print("Insira um valor válido")
    
if (__name__ == "__main__"):
    main()