# FOR = PARA CADA NUMBER
# IN = DA TABUADA

tabuada = [1,2,3,4,5,6,7,8,9,10]
número = int(input("Escolha a tabuada de um número: "))

for number in tabuada:
    print("A tabuada de {} x {} = {}".format(número, number, (número * number)))
