print("Descobrindo as seguintes propriedades: D=Densidade. M=Massa e V=Volume")

properties = input("Qual propriedade você quer descobrir?(D, M, V) ")

if properties == "D":
   M = float(input("Qual o valor da massa? "))
   V = float(input("Qual o valor do volume? "))
   result = M / V
   print(round(result, 3))
   
elif properties == "M":
   D = float(input("Qual o valor da densidade? "))
   V = float(input("Qual o valor do volume? "))
   result = D * V
   print(round(result, 3))

elif properties == "V":
   M = float(input("Qual o valor da massa? "))
   D = float(input("Qual o valor da densidade? "))
   result = M / D
   print(round(result, 3))

else:
   print(properties,"não é uma propriedade válida")