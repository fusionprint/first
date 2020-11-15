import projeto1
import projeto2

print('Qual jogo vc quer jogar: Dado(1) ou Acerte o número(2)')
opcao=input('>')

if (opcao == "1"):
    projeto1.jogue_o_dado()
elif (opcao == "2"):
    projeto2.guess_a_number()
