# OS COEFICIENTES FICAM POSITIVOS MESMO QUANDO O X1 E X2 SÃO NEGATIVOS


print("Coeficientes da equação do equação do 2º grau:")
print("------------------------------------------------")

x1= float(input("Digite o valor do x1: "))
x2= float(input("Digite o valor do x2: "))
print("------------------------------------------------")

c= (x1*x2)
a= (x1)*(x2) / c
b= -(x1+x2)
Delta = (b**2 - 4*a*c)

if a == 0:

    print("Operação invalida, pois o coeficiente A tem que ser diferente de zero")
    print("------------------------------------------------")

else:
    
    
    print("O valor do coeficiente a é: ", a)
    print("O valor do coeficiente b é: ", b)
    print("O valor do coeficiente c é: ", c)
    print("------------------------------------------------")

    print("E o seu delta é {:.2f}".format(Delta))
    print("------------------------------------------------")
