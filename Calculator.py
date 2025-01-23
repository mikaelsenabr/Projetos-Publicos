operator = input("Escolha os operadores (+ - * /): ")
quant = input("A operação será feita com 2 ou 3 números?: ")


if operator == "+":

  if quant == "2":
    num1 = float(input("Adicione o 1º número: "))
    num2 = float(input("Adicione o 2º número: "))
    result = num1 + num2
    print("{} + {}, é igual a {:.2f}".format(num1, num2, result))
  
  elif quant == "3":
    num1 = float(input("Adicione o 1º número: "))
    num2 = float(input("Adicione o 2º número: "))
    num3 = float(input("Adicione o 3º número: "))    
    result = num1 + num2 + num3
    print("{} + {} + {}, é igual a {:.2f}".format(num1, num2, num3, result))

  else:
      print("Escolha a operação com 2 ou 3 números apenas!!")

elif operator == "-":

  if quant == "2":
    num1 = float(input("Adicione o 1º número: "))
    num2 = float(input("Adicione o 2º número: "))
    result = num1 - num2
    print("{} - {}, é igual a {:.2f}".format(num1, num2, result))

  elif quant == "3":
    num1 = float(input("Adicione o 1º número: "))
    num2 = float(input("Adicione o 2º número: "))
    num3 = float(input("Adicione o 3º número: "))    
    result = num1 - num2 - num3
    print("{} - {} - {}, é igual a {:.2f}".format(num1, num2, num3, result))

  else:
      print("Escolha a operação com 2 ou 3 números apenas!!")

elif operator == "*":

  if quant == "2":
    num1 = float(input("Adicione o 1º número: "))
    num2 = float(input("Adicione o 2º número: "))
    result = num1 * num2
    print("{} * {} é igual a {:.2f}".format(num1, num2, result))

  elif quant == "3":
    num1 = float(input("Adicione o 1º número: "))
    num2 = float(input("Adicione o 2º número: "))
    num3 = float(input("Adicione o 3º número: "))    
    result = num1 * num2 * num3
    print("{} * {} * {}, é igual a {:.2f}".format(num1, num2, num3, result))

  else:
      print("Escolha a operação com 2 ou 3 números apenas!!")

elif operator == "/":     

  if quant == "2":
    num1 = float(input("Adicione o 1º número: "))
    num2 = float(input("Adicione o 2º número: "))
    result = num1 / num2
    print("{} / {} é igual a {:.2f}".format(num1, num2, result))

  elif quant == "3":
    num1 = float(input("Adicione o 1º número: "))
    num2 = float(input("Adicione o 2º número: "))
    num3 = float(input("Adicione o 3º número: "))    
    result = num1 / num2 / num3
    print("{} / {} / {}, é igual a {:.2f}".format(num1, num2, num3, result))

  else:
    print("Escolha a operação com 2 ou 3 números apenas!!")

else:
    print("{}, não é um operador válido".format(operator)) 
    