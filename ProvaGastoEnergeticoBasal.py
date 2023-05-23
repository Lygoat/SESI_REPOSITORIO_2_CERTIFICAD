import time

def aguarde(milissegundos):
    time.sleep(milissegundos / 1000)

def limpa():
    print("\n" * 100)

def inicio():
    aguarde(500)
    print("Bem vindo ao programa para calcular o gasto energetico basal\n")
    aguarde(1000)
    sexo = input("Por favor, digite seu sexo (Masculino ou Feminino): ")

    aguarde(1000)
    limpa()

    peso = float(input("Digite seu peso em kg: "))

    aguarde(1000)
    limpa()

    altura = float(input("Ok, agora digite sua altura em centimetros: "))

    aguarde(1000)
    limpa()

    idade = int(input("Para finalizar, digite sua idade: "))

    if sexo.lower() in ["masculino", "masculina", "masc", "masc"]:
        gastoEnergetico = 66 + (13.8 * peso) + (5.0 * altura) - (6.8 * idade)
    elif sexo.lower() in ["feminino", "feminina", "fem", "femin"]:
        gastoEnergetico = 655 + (9.6 * peso) + (1.9 * altura) - (4.7 * idade)
    else:
        print("Sexo não catalogado")
        return

    print("Seu gasto energetico basal é: {} KL".format(gastoEnergetico))

inicio()