#Jogo de adivinhação
import random


def jogar_adivinhacao():
    numero_secreto = random.randint(1,100)
    tentativas = 0
    max_tentativas = 10

    print('Bem-vindo ao jogo de adivinhação')
    print('Tente adivinha o número secreto entre 1 e 100')

    while tentativas < max_tentativas:
        tentativa = int(input('Digite o seu palpite: '))
        tentativas += 1

        if tentativa < numero_secreto:
            print('Digite um número maior')
        elif tentativa > numero_secreto:
            print('Digite um número menor')
        else:
            print(f'Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas(s)')
            break

    if tentativas == max_tentativas and tentativa != numero_secreto:
        print(f'Fim do jogo! O número secreto era {numero_secreto}. Tente novamente')

jogar_adivinhacao()