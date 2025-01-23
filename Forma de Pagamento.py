#FORMA DE PAGAMENTO

v = float(input("Qual o valor do produto? R$"))
forma_pagamento = input("Qual a forma de pagamento (a vista, parcelado)? ").lower()

if forma_pagamento == "a vista" :
    total = v - (v * 0.10)
    print("O valor total da sua compra é de R${:.2f}".format(total))

elif forma_pagamento == "parcelado" :
    total = v + (v * 0.08)
    print("O valor total da sua compra é de R${:.2f}".format(total))

else:
    print("Forma de Pagamento Incorreta. Escolha (a vista, parcelado)")
    