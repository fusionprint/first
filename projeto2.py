import random

print("#####Guess a number#####")

numero = random.randrange(1, 11)

chute = int(input(('Chute um número:')))

while (chute != numero):
    if (chute > numero):
        print("Seu chute foi alto")
        chute=int(input("Tente de novo:"))
    if (chute < numero):
        print("Seu chute foi baixo")
        chute=int(input("Tente de novo:"))
else:
    print("Você ganhou!")

