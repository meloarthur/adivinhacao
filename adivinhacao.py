from random import randint, random

print("***************************************")
print("Bem-vindo ao jogo de adivinhação!")
print("***************************************")

print(">>> REGRAS")
print("1- Três chances para acertar")
print("2- O seu palpite deve ser um número de 1 a 10")
print("3- Números não decimais\n")

numero_secreto = randint(1,10)
chances = 0
chute = 0

while chute != numero_secreto:
    chute = input("Palpite {} de 3 -> ".format(chances+1))
    chute = int(chute)
    chances += 1
    if chute == numero_secreto:
        print("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$_____$$$$
$$$$_____$$$$$$$$$$$$$$$_____$$$$
$$$$_____$$$$$$$$$$$$$$$_____$$$$
$$$$_____$$____$$$____$$_____$$$$
$$$$_____$______$______$_____$$$$
$$$$_____$______$______$_____$$$$
$$$$_____$____$$$$$$$$$$$$$$$$$$$
$$$$_____$___$$___________$$$$$$$
$$$$_____$__$$_______________$$$$
$$$$__________$$_____________$$$$
$$$$___________$$___________$$$$$
$$$$_____________$_________$$$$$$
$$$$$_____________________$$$$$$$
$$$$$$___________________$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
        print("PARABÉNS, VOCÊ ACERTOU!\n")
        break;
    else:
        print("Você errou...\n".format(chances))
    if chances == 3:
        print("""
``````````````$$$$$$$$$$$\_/$$$$$$$$$$$`````````````
``````````````$$$$$$$$$$$$$$$$$$$$$$$$$$````````````
`````````````$$$$$$`$$$$$$$$$$$$$$`$$$$$````````````
``$`$```````$$$$$$$```$$$$$$$$$$$``$$$$$$````$``$``$
``$`$``$````$$$$$$$````$$$$$$$$````$$$$$$`````$`$`$`
$`$`$`$````$$$$$$$$``````$$$$``````$$$$$$$````$$$$$`
`$$$$$`````$$$$$$$$```O`$$$$$``O``$$$$$$$$`$$$$$$$``
`$$$$$$$$``$$$$$$$$$````$$$$$$````$$$$$$$$$$```$$$``
````$$````$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$`$$````$$``
````$`````$$$`$$$$$$$$$$$$$$$$$$$$$$$$$$``$$````````
``````````$$$``$$$$$$$$$$$$$$$$$$$$$$$$``$$$````````
``````````$$$``$$$$$$$$$$$$$$$$$$$$$$$$``$$$````````
```````````$$$`````$$$$$$$$$$$$$$$$`````$$``````````
````````````$$````````$$$$$$$$$$```````$$```````````
`````````````$$$``````$$$````$$$```````$````````````
```````````````$$`````$$``````$$``````$`````````````
````````````````$$$```$````````$`````$``````````````
```````````````````$$$``````````````$```````````````
``````````````````````$$$$$$$$$$$$$````````````````""")
        print("O número era", numero_secreto)
        print("VOCÊ PERDEU!\n")
        break;

input("Pressione Enter para encerrar...")