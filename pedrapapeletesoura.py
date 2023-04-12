import random
import sys

# Pedra = 1, Papel = 2, Tesoura = 3
jogarmais = "SIM"
while jogarmais == "SIM":
    escolha = input("Digite PEDRA, PAPEL ou TESOURA: ")
    if escolha != "PEDRA" and escolha != "PAPEL" and escolha != "TESOURA":
        print("Escolha Inválida")
        continue

    escolharobo = random.randint(1, 3)

    match escolha:
        case "PEDRA":
            if escolharobo == 1:
                print("VOCÊ ESCOLHEU {}".format(escolha))
                print("SEU OPONENTE ESCOLHEU PEDRA")
                print("EMPATE")
            elif escolharobo == 2:
                print("VOCÊ ESCOLHEU {}".format(escolha))
                print("SEU OPONENTE ESCOLHEU PAPEL")
                print("SEU OPONENTE GANHOU")
            elif escolharobo == 3:
                print("VOCÊ ESCOLHEU {}".format(escolha))
                print("SEU OPONENTE ESCOLHEU TESOURA")
                print("VOCÊ GANHOU")
        case "PAPEL":
            if escolharobo == 1:
                print("VOCÊ ESCOLHEU {}".format(escolha))
                print("SEU OPONENTE ESCOLHEU PEDRA")
                print("VOCÊ GANHOU")
            elif escolharobo == 2:
                print("VOCÊ ESCOLHEU {}".format(escolha))
                print("SEU OPONENTE ESCOLHEU PAPEL")
                print("EMPATE")
            elif escolharobo == 3:
                print("VOCÊ ESCOLHEU {}".format(escolha))
                print("SEU OPONENTE ESCOLHEU TESOURA")
                print("SEU OPONENTE GANHOU")
        case "TESOURA":
            if escolharobo == 1:
                print("VOCÊ ESCOLHEU {}".format(escolha))
                print("SEU OPONENTE ESCOLHEU PEDRA")
                print("SEU OPONENTE GANHOU")
            elif escolharobo == 2:
                print("VOCÊ ESCOLHEU {}".format(escolha))
                print("SEU OPONENTE ESCOLHEU PAPEL")
                print("VOCÊ GANHOU")
            elif escolharobo == 3:
                print("VOCÊ ESCOLHEU {}".format(escolha))
                print("SEU OPONENTE ESCOLHEU TESOURA")
                print("EMPATE")

    jogarmais = input("QUER CONTINUAR JOGANDO? (SIM/NAO): ")
    if jogarmais == "SIM":
        continue
    else:
        sys.exit()
