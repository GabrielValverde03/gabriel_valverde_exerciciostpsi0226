saldo=int(input("Insira o seu saldo:"))
cheque=int(input("Insira o cheque a descontar:"))

if saldo > cheque:
    print(f"Cheque descontado, saldo: {saldo - cheque}")
else:
    print("Cheque não pode ser descontado, saldo insuficiente")