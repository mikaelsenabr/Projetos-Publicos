# APRENDER ESTRUTURA DE REPETIÇÃO WHILE!!
# COLOCAR A PERGUNTA SEMPRE DENTRO WHILE, PARA QUANDO O RESULTADO NÃO FOR CORREPONDENTE, O PROGRAMA REFAZER A PERGUNTA!
# Tratamento de Erros de Entrada: O código acima pode gerar um erro ValueError se o usuário digitar algo que não pode ser convertido para um inteiro (por exemplo, letras ou símbolos). Adicionar um bloco try/except resolve esse problema:

import random

número = random.randint(1, 100)

while True:
    try:
        chute = int(input("Chute um número: "))
        print("-"*32)

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        print("-"*32)
        continue  # Volta para o início do loop
    
    if chute < número:
        print("Chute um número maior!")
        print("-"*32)

    elif chute > número:
        print("Chute um número menor")
        print("-"*32)

    else:
        print("Parabéns, você adivinhou o número escolhido!")
        print("-"*32)
        break
