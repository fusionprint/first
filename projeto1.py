import random

def jogue_o_dado():
    opcao=(input("Você gostaria de jogar o dado? (s) ou (n): "))


    while opcao == "s":
        numero = random.randrange(1, 7)
        print("Você tirou o número:", numero)
        opcao = str(input(("Você quer jogar de novo? (s) ou (n)")))
    else:
        print('Ok bye')
    jogue_o_dado()











