import random
from warnings import simplefilter
tentativas = []
def show_score():
    if len(tentativas) <= 0:
        print("Ainda não há um recorde, você pode ser o primeiro!")
    else:
        print("O recorde atual é {} tentativas".format(min(tentativas)))
def start_game():
    random_number = int(random.randint(1,10))
    print("Olá héroi, bem vindo ao jogo de advinhação")
    jogador = input("Qual o seu nome?\n")
    jogar = input(f"Olá {jogador}, você gostarias de jogar um jogo? (Sim ou Não)\n")
    chutes = 0
    show_score()
    while jogar.lower() == "sim":
        try:
            guess = int(input("Escolha um número de 1 até 10\n"))
            if guess < 1 or guess > 10:
                raise ValueError("Por favor escolha um valor de 1 a 10.\n")
            elif guess == random_number:
                print("Parabéns héroi, você acertou!\n")
                chutes += 1
                tentativas.append(chutes)
                jogar_novamente = input(f"Você precisou de {chutes} tentativas, gostaria de continuar? (Sim ou Não)\n")
                chutes = 0
                random_number = int(random.randint(1,10))
                show_score()
                if jogar_novamente.lower() == "nao":
                    print(f"Que pena {jogador}, foi um bom jogo héroi")
                    break
            elif guess < random_number:
                maior = ["Quase, um pouco maior", "É um número maior", "Passou perto, um pouco mais"]
                print(random.choice(maior))
                chutes += 1
            elif guess > random_number:
                menor = ["É um número menor", "Um pouco menos", "Perto, héroi um pouco menos"]
                print(random.choice(menor))
                chutes += 1        
        except ValueError as err:
            print (f"Este não é um valor valido {jogador} tente novamente")
            print(f"{err}")
    else:
            print(f"Que pena, seria uma boa partida {jogador}, Tenha um ótimo dia.")

if __name__ == '__main__':
    start_game()            