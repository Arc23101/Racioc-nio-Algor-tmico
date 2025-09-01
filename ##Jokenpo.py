##Jokenpô(Antony V Braghini)

import random
Modalidade = 0
Player1 = 0
nomeP1 = "Player 1"
escolhaPlayer1 = 0
vPlayer1 = 0
player2 = 0
nomeP2 ="Player 2"
vPlayer2 = 0
escolhaPlayer2 = 0
bot1 = 0
vBot1 = 0
escolhaBot1 = 0
bot2 = 0
vBot2 = 0
escolhaBot2 = 0
continuar = 1
modalidade = int(input("Qual modalidade você vai querer: \n1 para humanao vs humano \n2 para humano vs bot \n3 para bot vs bot: "))
if modalidade < 1 or modalidade > 3:
        modalidade = int(input("Numero inválido digite Novamente: \n1 para humanao vs humano \n2 para humano vs bot \n3 para bot vs bot: "))
if modalidade == 1:
    nomeP1 = input("Digite o nome do player 1: ")
    nomeP2 = input("Digite o nome do player 2: ")
    while continuar == 1:
        escolhaPlayer1 = int(input("Digite 1 para tesoura, 2 para Pedra e 3 para papel: "))
        if escolhaPlayer1 < 1 or escolhaPlayer1 > 3:
            escolhaPlayer1 = int(input("Numero inválido digite Novamente, 1 para tesoura, 2 para Pedra e 3 para papel: "))
        escolhaPlayer2 = int(input("Digite 1 para tesoura, 2 para Pedra e 3 para papel: "))
        if escolhaPlayer2 < 1 or escolhaPlayer2 > 3:
            escolhaPlayer2 = int(input("Numero inválido digite Novamente, 1 para tesoura, 2 para Pedra e 3 para papel: "))
        if escolhaPlayer1 == escolhaPlayer2:
            print(f"Empate \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 1 and escolhaPlayer2 == 2:
            vPlayer2 += 1
            print(f"Player 2 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 1 and escolhaPlayer2 == 3:
            vPlayer1 += 1
            print(f"Player 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 2 and escolhaPlayer2 == 1:
            vPlayer1 += 1
            print(f"Player 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 2 and escolhaPlayer2 == 3:
            vPlayer2 += 1
            print(f"Player 2 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 3 and escolhaPlayer2 == 1:
            vPlayer2 += 1
            print(f"Player 2 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 3 and escolhaPlayer2 == 2:
            vPlayer1 += 1
            print(f"Player 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
elif modalidade == 2:
    nomeP1 = input("Digite o nome do player 1: ")
    while continuar == 1:
        escolhaPlayer1 = int(input("Digite 1 para tesoura, 2 para Pedra e 3 para papel: "))
        if escolhaPlayer1 < 1 or escolhaPlayer1 > 3:
            escolhaPlayer1 = int(input("Numero inválido digite Novamente, 1 para tesoura, 2 para Pedra e 3 para papel: "))
        escolhaBot1 = (random.randint(1,3))
        if escolhaPlayer1 == escolhaBot1:
            print(f"Empate \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \nBot 1 ganhou {vBot1}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 1 and escolhaBot1 == 2:
            vBot1 += 1
            print(f"Bot 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \nBot1 ganhou {vBot1}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 1 and escolhaBot1 == 3:
            vPlayer1 += 1
            print(f"Player 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \nBot 1 ganhou {vBot1}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 2 and escolhaBot1 == 1:
            vPlayer1 += 1
            print(f"Player 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \nBot 1 ganhou {vBot1}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 2 and escolhaBot1 == 3:
            vBot1 += 1
            print(f"Bot 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \nBot 1 ganhou {vBot1}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 3 and escolhaBot1 == 1:
            vBot1 += 1
            print(f"Bot 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \nBot 1 ganhou {vBot1}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaPlayer1 == 3 and escolhaBot1 == 2:
            vPlayer1 += 1
            print(f"Player 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \nBot 1 ganhou {vBot1}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
elif modalidade == 3:
    while continuar == 1:
        escolhaBot1 = (random.randint(1,3))
        escolhaBot2 = (random.randint(1,3))
        if escolhaBot1 == escolhaBot2:
            print(f"Empate \naqui esta o placar Geral: \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaBot1 == 1 and escolhaBot2 == 2:
            vBot2 += 1
            print(f"Bot 2 ganhou \naqui esta o placar Geral: \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaBot1 == 1 and escolhaBot2 == 3:
            vBot1 += 1
            print(f"Bot 1 ganhou \naqui esta o placar Geral: \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaBot1 == 2 and escolhaBot2 == 1:
            vBot1 += 1
            print(f"Bot 1 ganhou \naqui esta o placar Geral: \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaBot1 == 2 and escolhaBot2 == 3:
            vBot2 += 1
            print(f"Bot 1 ganhou \naqui esta o placar Geral: \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaBot1 == 3 and escolhaBot2 == 1:
            vBot2 += 1
            print(f"Bot 1 ganhou \naqui esta o placar Geral: \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
        elif escolhaBot1 == 3 and escolhaBot2 == 2:
            vBot1 += 1
            print(f"Bot 1 ganhou \naqui esta o placar Geral: \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2}")
            continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
            if continuar < 0 or continuar > 1:
                continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
print(f"aqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2} \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2} \nObrigado por jogar")