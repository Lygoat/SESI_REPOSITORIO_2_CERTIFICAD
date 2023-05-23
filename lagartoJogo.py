import random

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]
    resultado = {
        "pedra": ["tesoura", "lagarto"],
        "papel": ["pedra", "spock"],
        "tesoura": ["papel", "lagarto"],
        "lagarto": ["papel", "spock"],
        "spock": ["pedra", "tesoura"]
    }

    while True:
        jogador = input("Escolha sua jogada (pedra, papel, tesoura, lagarto, spock): ")
        jogador = jogador.lower()

        if jogador in opcoes:
            computador = random.choice(opcoes)

            print("Computador escolheu:", computador)

            if jogador == computador:
                print("Empate!")
            elif computador in resultado[jogador]:
                print("Você venceu!")
            else:
                print("Você perdeu!")

            break
        else:
            print("Escolha inválida. Tente novamente.")

jogar_jokenpo()
