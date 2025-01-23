import pygame

print("Equação do 2º grau:")
print("-"*32)

a = float(input("o valor do coeficiente A é: "))
b = float(input("o valor do coeficiente B é: "))
c = float(input("O valor do coeficiente C é: "))
print("-"*32)

Delta = (b**2 - 4*a*c)

x1 = (-b + Delta**0.5) / (2*a)
x2 = (-b - Delta**0.5) / (2*a)

print("O seu Delta é {:.2f}".format(Delta))
print("-"*32)


if Delta < 0:
    
    print("Para Delta negativo, não existe raízes Reais")
    print("-"*32)

elif Delta == 0:
    
    print("Sendo Delta igual a zero, temos duas raízes iguais a {} ".format(x1))
    print("-"*32)
    
else:

    if a == 0:

        print("Operação invalida, pois o coeficiente A tem que ser diferente de zero")
        print("-"*32)

    else:
 
        print("O valor do x1 é: {:.2f}".format(x1))
        print("O valor do x2 é: {:.2f}".format(x2))
        print("-"*32)
            