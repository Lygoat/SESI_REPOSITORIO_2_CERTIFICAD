import random#gerador de numeros
import time# delay de tela

def main():#definiçao de funçao
    print("Bem vindo ao jogo...")
    verificador = input("Pressione (n) para começar: ")
    
    while verificador.lower() == "n":#o . lower serve para dizer que a string n tambem pode ser N maiusculo em vez de ficar botando and 
        print("Mas que jogo?")
        time.sleep(1)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".\n")
        time.sleep(1)
        print("=================")
        print(" JOGO DO BIXO!!!")
        print("================\n")
        time.sleep(2)
        clear_screen()#limpando o terminal
        
        numero = int(input("Digite seu numero de aposta: "))
        valor = float(input("Digite o valor que você pagou pela aposta sem o cifrão: "))
        clear_screen()
        
        sorteado = random.randint(1, 25)
        print("Número sorteado pela banca foi", sorteado)
        
        if sorteado == numero:
            print(numero, "parabéns, você venceu! Seu prêmio é de:", valor * 18, "R$")
        else:
            print("Tente novamente, animal sorteado:")
        
        if sorteado == 1:
            print("avestruz")
        elif sorteado == 2:
            print("burro")
        elif sorteado == 3:
            print("borboletas")
        elif sorteado == 4:
            print("cachorro")
        elif sorteado == 5:
            print("cabra")
        elif sorteado == 6:
            print("carneiro")
        elif sorteado == 7:
            print("camelo")
        elif sorteado == 8:
            print("cobra")
        elif sorteado == 9:
            print("coelho")
        elif sorteado == 10:
            print("cavalo")
        elif sorteado == 11:
            print("elefante")
        elif sorteado == 12:
            print("galo")
        elif sorteado == 13:
            print("gato")
        elif sorteado == 14:
            print("jacaré")
        elif sorteado == 15:
            print("leão")
        elif sorteado == 16:
            print("macaco")
        elif sorteado == 17:
            print("porco")
        elif sorteado == 18:
            print("pavão")
        elif sorteado == 19:
            print("peru")
        elif sorteado == 20:
            print("touro")
        elif sorteado == 21:
            print("tigre")
        elif sorteado == 22:
            print("urso")
        elif sorteado == 23:
            print("veado")
        elif sorteado == 24:
            print("vaca")
        
        time.sleep(4)
        clear_screen()
        
        verificador = input("Deseja jogar novamente? Pressione (n) para iniciar uma nova partida ou (e) para sair: ")
        clear_screen()
    
    print("Obrigado por ver nossa aplicação.")

def clear_screen():
    print("\033c", end="")  # ANSI escape sequence to clear the screen

if __name__ == "__main__":
    main()
