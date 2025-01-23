print("J = C ∙ I ∙ T, em que J é o juros, C é o capital, I é a taxa de juros e T é o tempo em meses.")

operator = input("Qual você quer descobrir: (J, C, I, T): ").upper()

if operator == "J":
    C = float(input("O valor do Capital é igual a: "))
    I = float(input("O valor da taxa de juros ao mês  é igual a: "))
    T = float(input("A quantidade de Tempo em meses é igual a: "))
    J = C * (I / 100) * T
    print("O valor do juros é igual a R${:.2f}.".format(J))

elif operator == "C":
    J = float(input("O valor do juros ao mês  é igual a: "))
    I = float(input("O valor da taxa de juros ao mês  é igual a: "))
    T = float(input("A quantidade de tempo em meses é igual a: "))
    C = J * 100 / ( I * T)
    print("O valor do capital é igual a R${}.".format(C))

elif operator == "I":
    J = float(input("O valor do juros ao mês  é igual a: "))
    C = float(input("O valor do Capital é igual a: "))
    T = float(input("A quantidade de Tempo em meses é igual a: "))
    I = J / (C * T)
    print("O valoor do juros é igual a {}%.".format(I))

elif operator == "T":
    J = float(input("O valor do juros ao mês  é igual a: "))
    C = float(input("O valor do Capital é igual a: "))
    I = float(input("O valor da taxa de juros ao mês  é igual a: "))
    T = J / (C * I / 100)
    print("A quantidade de tempo é igual a {} mês/meses.".format(T))
    
else:
    print(operator,"não é um operador válido") 