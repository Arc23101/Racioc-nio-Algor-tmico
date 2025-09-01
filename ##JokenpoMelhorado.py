##Jokenpo(Antony V Braghini)
import random
def coletarJogadaHumano():
    escolhaPlayer = int(input("Digite 1 para tesoura, 2 para Pedra e 3 para papel: "))
    while escolhaPlayer < 1 or escolhaPlayer > 3:
        escolhaPlayer = int(input("Numero inválido digite Novamente, 1 para tesoura, 2 para Pedra e 3 para papel: "))
    return escolhaPlayer
def verificarGanhador(escolhaPlayer1, escolhaPlayer2):
    if escolhaPlayer1 == escolhaPlayer2:
        return 0
    elif escolhaPlayer1 == 1 and escolhaPlayer2 == 2 or escolhaPlayer1 == 2 and escolhaPlayer2 == 3 or escolhaPlayer1 == 3 and escolhaPlayer2 ==1:
            return 2
    else:
        return 1
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
if modalidade < 3:
    nomeP1 = input("Digite o nome do player 1: ")
    if modalidade < 2
        nomeP2 = input("Digite o nome do player 2: ")
while continuar == 1:
    if modalidade == 1:
        escolhaPlayer1 = coletarJogadaHumano()
        escolhaPlayer2 = coletarJogadaHumano()
        resultado = verificarGanhador(escolhaPlayer1,escolhaPlayer2)
        if resultado == 0 :
                print(f"Empate \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2} ")
        elif resultado == 1:
                vPlayer1 += 1
                print(f"Player 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2} ")
        else:
                vPlayer2 += 1
                print(f"Player 2 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2} ")
    elif modalidade == 2:
        escolhaBot1 = (random.randint(1,3))
        escolhaPlayer1 = coletarJogadaHumano()
        resultado = verificarGanhador(escolhaPlayer1,escolhaBot1)
        if resultado == 0 :
                print(f"Empate \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \nBot 1 ganhou {vBot1} ")
        elif resultado == 1:
                vPlayer1 += 1
                print(f"Player 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \nBot 1 ganhou {vBot1} ")
        else:
                vBot1 += 1
                print(f"Bot 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \nBot 1 ganhou {vBot1} ")
    elif modalidade == 3:
        escolhaBot1 = (random.randint(1,3))
        escolhaBot2 = (random.randint(1,3))
        resultado = verificarGanhador(escolhaBot1,escolhaBot2)
        if resultado == 0 :
                print(f"Empate \naqui esta o placar Geral: \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2} ")
        elif resultado == 1:
                vBot1 += 1
                print(f"Bot 1 ganhou \naqui esta o placar Geral: \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2} ")
        else:
                vBot2 += 1
                print(f"Bot 2 ganhou \naqui esta o placar Geral: \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2} ")
    continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
    if continuar < 0 or continuar > 1:
        continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
print(f"aqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2} \nBot 1 ganhou {vBot1} \nBot 2 ganhou {vBot2} \nObrigado por jogar")