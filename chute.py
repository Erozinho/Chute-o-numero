import random
from time import sleep
import os
A = True
while A == True:
    NUM = random.randint(0,100)
    print("CHUTE UM NUMERO!!!!\nDigite um valor entre 0 a 100 inteiros e tente adivinhar o numero!")
    while True:
        VAL = int(input())
        if VAL > NUM:print("Você chutou alto diminui ai")
        if VAL < NUM:print("Você chutou baixo aumenta ai")
        if VAL == NUM:
            print("Boa acertou o numero!\nO numero era {}".format(NUM))
            break
    A = int(input("Quer jogar dnv? (1-sim/2-não)"))
    if A == 1: 
        A = True
        os.system("CLS")
    if A == 2:
        print("Fechando o programa em 5 segundos!")
        sleep(5)
        quit()
