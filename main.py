#Jogo de adivinhação

import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1,100)
    tentativa = 0
    max_tentativas = 10

    