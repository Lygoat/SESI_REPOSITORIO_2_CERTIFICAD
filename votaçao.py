import time

def aguarde(milissegundos):
    time.sleep(milissegundos / 1000)

def limpa():
    print("\n" * 100)

def inicio():
    nome = input("ASSINE O SEU NOME COMPLETO:--> ")
    print("\nOlá,", nome, "Vamos agora passar as instruções e os candidatos\n")
    aguarde(1000)
    print(".")
    aguarde(1000)
    print(".")
    aguarde(1000)
    print(".")
    aguarde(1000)
    limpa()

    lula = 0
    bolsonaro = 0
    galo = 0
    nativo = 0
    kunavara = 0
    jacinto = 0
    brancos = 0
    nulos = 0
    total_votos = 0

    while True:
        print("=====================================================")
        aguarde(500)
        print("                   CANDIDATOS 2023                   ")
        aguarde(500)
        print("=====================================================")
        aguarde(1000)
        print("Candidato inacio lula ---> 1")
        aguarde(1000)
        print("Candidato mesias bolsonaro ---> 2")
        aguarde(1000)
        print("Candidato Galo Seco ---> 3")
        aguarde(1000)
        print("Candidato Nativo Pata Chota ---> 4")
        aguarde(1000)
        print("Candidato kunavara da Silva ---> 5")
        aguarde(1000)
        print("Candidato Jacinto leite ---> 6")
        aguarde(1000)
        print("Branco ---> 7")
        aguarde(1000)
        print("Nulo ---> 8")
        aguarde(1000)
        print("Para parar o programa e ver os resultados finais digite 0")
        voto = int(input("Digite seu voto: "))
        limpa()

        while voto == 1 or voto == 2:
            print("Candidato inelegível. Digite outro por favor: ")
            voto = int(input("Digite seu voto: "))

        if voto == 0:
            print("Votação encerrada!\n")
            break
        elif voto == 6:
            jacinto += 1
        elif voto == 5:
            kunavara += 1
        elif voto == 4:
            nativo += 1
        elif voto == 3:
            galo += 1
        elif voto == 2:
            bolsonaro += 1
        elif voto == 1:
            lula += 1
        elif voto == 7:
            brancos += 1
        else:
            nulos += 1

    total_votos = lula + bolsonaro + galo + nativo + kunavara + jacinto + brancos + nulos

    if total_votos > 0:
        porcLula = (lula * 100.0) / total_votos
        porcJair = (bolsonaro * 100.0) / total_votos
        porKunavara = (kunavara * 100.0) / total_votos
        porcGalo = (galo * 100.0) / total_votos
        porcJacinto = (jacinto * 100.0) / total_votos
        porcNativo = (nativo * 100.0) / total_votos
        porcBrancos = (brancos * 100.0) / total_votos
        porcNulo = (nulos * 100.0) / total_votos

        print("\n")
        print("Total de votos:", total_votos)
        print("Candidato Galo Seco:", galo, "votos. ", porcGalo, "% do total")
        print("Candidato Nativo Pata Chota:", nativo, "votos. ", porcNativo, "% do total")
        print("Candidato Kunavara da Silva:", kunavara, "votos. ", porKunavara, "% do total")
        print("Candidato Jacinto leite:", jacinto, "votos. ", porcJacinto, "% do total")
        print("Candidato Mesias Bolsonaro:", bolsonaro, "votos. ", porcJair, "% do total")
        print("Candidato Inacio Lula:", lula, "votos. ", porcLula, "% do total")
        print("Brancos:", brancos, "voto(s).", porcBrancos, "% do total")
        print("Nulos:", nulos, "voto(s).", porcNulo, "% do total")

inicio()
