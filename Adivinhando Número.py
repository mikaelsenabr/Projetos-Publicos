# APRENDER ESTRUTURA DE REPETIÇÃO WHILE!!
# COLOCAR A PERGUNTA SEMPRE DENTRO WHILE, PARA QUANDO O RESULTADO NÃO FOR CORREPONDENTE, O PROGRAMA REFAZER A PERGUNTA!

import random

print("Adivinhando o número escolhido entre 0 e 10:")
print("-"*32)

número_escolhido = random.randint(0, 10)

while True:
        chute = int(input("Chute qual número foi escolhido: "))
        print("-"*32)

        if chute < número_escolhido:
                print("Chute um número maior!: ")
                print("-"*32)

        elif chute > número_escolhido:
                print("Chute um número menor!: ")
                print("-"*32)

        else:
                print("Parabéns, você acertou o número escolhido!!")
                print("-"*32)
                break
