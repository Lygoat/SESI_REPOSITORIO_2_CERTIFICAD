import random

def inicio():
    ppt = ["pedra", "papel", "tesoura"]
    computador = random.choice(ppt)
    jogador = input("Escolha sua jogada - pedra, papel ou tesoura: ")
    print("\nA escolha da máquina foi:", computador)

    while jogador == computador:
        print("\nEmpate!")
        return

    if (computador == "pedra" and jogador == "papel") or (computador == "papel" and jogador == "tesoura") or (computador == "tesoura" and jogador == "pedra"):
        print("Você venceu!")
    else:
        print("Você perdeu!")

inicio()