##Jokenpô(Antony V Braghini)
import random
resultadosVitoria = [[0, 2, 1],
                     [1, 0, 2],
                     [2, 1, 0]]
jogadas = ["tesoura", "pedra", "papel"]
def coletarJogadaHumano():
    escolhaPlayer = str(input("Digite tesoura, Pedra ou papel(A frase se repete quando é a vez do proximo player): "))
    while escolhaPlayer not in jogadas:
        escolhaPlayer = str(input("Inválido digite Novamente, tesoura, Pedra ou papel: "))
    if escolhaPlayer =="tesoura":
        escolhaPlayer = 0
    elif escolhaPlayer =="pedra":
        escolhaPlayer = 1
    elif escolhaPlayer =="papel":
        escolhaPlayer = 2
    return escolhaPlayer

def coletarJogadaBot():
    escolhaBot = random.randint(1,3)
    return escolhaBot

def verificarGanhador(escolhaPlayer1, escolhaPlayer2):
    if escolhaPlayer1 == escolhaPlayer2:
        return 0
    elif resultadosVitoria[escolhaPlayer1] [escolhaPlayer2] == 2:
            return 2
    else:
        return 1
def Jogo():
    global vPlayer1,vPlayer2, continuar
    if modalidade == 1:
            escolhaPlayer1 = coletarJogadaHumano()
            escolhaPlayer2 = coletarJogadaHumano()
    elif modalidade == 2:
            escolhaPlayer1 = coletarJogadaHumano()
            escolhaPlayer2 = coletarJogadaBot()
            print(f"Player 2 escolheu {escolhaPlayer2}")
    elif modalidade == 3:
            escolhaPlayer1 = coletarJogadaBot()
            escolhaPlayer2 = coletarJogadaBot()
            print(f"Player 1 escolheu {escolhaPlayer1} \nE o Player 2 escolheu {escolhaPlayer2}")
    resultado = verificarGanhador(escolhaPlayer1,escolhaPlayer2)
    if resultado == 0 :
            print(f"Empate \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2} ")
    elif resultado == 1:
            vPlayer1 += 1
            print(f"Player 1 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2} ")
    else:
            vPlayer2 += 1
            print(f"Player 2 ganhou \naqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2} ")
    continuar = int(input("Gostaria de continuar? se sim digite 1, se não digite 0: "))
    if continuar < 0 or continuar > 1:
            continuar = int(input("Numero inválido digite Novamente se sim digite 1, se não digite 0: "))
    if  continuar == 1:
        Jogo()
    else:
        return 0
    
nomeP1 = "Player 1"
escolhaPlayer1 = 0
vPlayer1 = 0
nomeP2 ="Player 2"
vPlayer2 = 0
escolhaPlayer2 = 0
continuar = 1

modalidade = int(input("Qual modalidade você vai querer: \n1 para humanao vs humano \n2 para humano vs bot \n3 para bot vs bot: "))
while modalidade < 1 or modalidade > 3:
    modalidade = int(input("Numero inválido digite Novamente: \n1 para humanao vs humano \n2 para humano vs bot \n3 para bot vs bot: "))
if modalidade < 3:
    nomeP1 = input("Digite o nome do player 1: ")
    if modalidade < 2:
        nomeP2 = input("Digite o nome do player 2: ")
Jogo()

print(f"aqui esta o placar Geral: \n{nomeP1} ganhou {vPlayer1} \n{nomeP2} ganhou {vPlayer2} \nObrigado por jogar")
