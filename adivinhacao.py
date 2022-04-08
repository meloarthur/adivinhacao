from random import randint, random

print("***************************************")
print("Bem vindo ao jogo de adivinhação!")
print("***************************************")

print("\n>>>Três chances para acertar<<<\n")

numero_secreto = randint(1,10) 
chute_str = input("Digite o número secreto de 1 a 10: ")
chute = int(chute_str)
i=0

while i < 2:
    if chute == numero_secreto:
        print("Parabéns, você acertou!\n")
        break
    else:
        print("Você errou...\n")
        i += 1
        chute_str = input("Digite o número secreto de 1 a 10: ")
        chute = int(chute_str)
        
if i >= 2:
    print("Você errou...\n")
    print("O número era", numero_secreto)
    print("Que pena, suas chances acabaram. Mais sorte da próxima vez!\n")