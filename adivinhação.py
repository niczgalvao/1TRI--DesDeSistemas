#importaçao da bibliotecq
import random
#sorteio de numero aleatório
numero = random.randint (0,10)
print (numero)

tentativas = 1 
while (tentativas <= 3):
    print("tentaviva:", tentativas)
    chute = int(input ("digite o seu chute (0 a 10): "))
    if chute == numero:
        print("uiiii que cara sortudo")
        break
    else:
        print("desista")
    tentativas = tentativas +1 
print("ACABOU")