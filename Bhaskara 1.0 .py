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

print("O valor do x1 é: {:.2f}".format(x1))
print("O valor do x2 é: {:.2f}".format(x2))
print("-"*32)
            