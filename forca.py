def jogar():
    print("************************************")
    print("Bem vindo ao jogo de forca          ")
    print("************************************")
    
    palavra_secreta = "banana"
    

    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 0


    print(letras_acertadas)

    while(not enforcou and not acertou):
    
        chute = input("Qual letra?") #strip corta os espaços em branco
        chute = chute.strip()
        
        if(chute.upper() in palavra_secreta.upper()):
            posicao = 0

            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[posicao] = letra
                posicao = posicao + 1
        else:
            erros+= 1

        print(letras_acertadas)
        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
    if(enforcou):
        print("Você perdeu!")
    elif(acertou):
        print("Você venceu!")

    print("Fim do jogo")

# Verifica se o python foi executado do terminal
if(__name__ == "__main__"):
    jogar()