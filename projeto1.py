import random

opcao=(input("Você gostaria de jogar o dado? (s) ou (n): "))

while opcao == "s":
    print(random.randrange(1, 7))
    print("#####################")
    opcao = str(input(("Você quer jogar de novo? (s) (n)")))
else:
    print('Ok bye')











