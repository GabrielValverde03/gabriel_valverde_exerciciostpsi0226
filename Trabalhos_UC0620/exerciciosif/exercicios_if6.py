cliente=(input("Digite o seu nome:"))
valorcompra=float(input("Digite o valor da sua compra:"))
desconto = 0.00

if valorcompra <= 200.00:
    desconto = valorcompra * 0.10
    print(f"Nome: {cliente}")
    print(f"Compra: {valorcompra}€")
    print(f"Desconto: {desconto}€")
    print(f"Total a pagar:{valorcompra - desconto}€")
elif valorcompra >= 200.01 and valorcompra <=500.00:
    desconto = valorcompra * 0.15
    print(f"Nome: {cliente}")
    print(f"Compra: {valorcompra}€")
    print(f"Desconto: {desconto}€")
    print(f"Total a pagar:{valorcompra - desconto}€")
else:
    desconto = valorcompra * 0.20
    print(f"Nome: {cliente}")
    print(f"Compra: {valorcompra}€")
    print(f"Desconto: {desconto}€")
    print(f"Total a pagar:{valorcompra - desconto}€")
