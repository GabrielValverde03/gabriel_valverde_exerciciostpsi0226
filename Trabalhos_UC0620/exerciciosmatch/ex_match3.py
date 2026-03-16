dic = {"tipo": "","valor":""}

tipo = input("Insira se é compra ou venda:")
valor = input("Insira o valor:")

dic.update({"tipo": tipo})
dic.update({"valor": valor})

match tipo:
    case "venda" | "compra":
        print(f"{tipo} de {valor} €")
    case _:
        print("Pedido desconhecido")