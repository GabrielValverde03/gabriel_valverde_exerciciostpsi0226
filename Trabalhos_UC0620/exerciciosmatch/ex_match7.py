dic = {"categoria": "","preco": 0.0}

categoria = input("Insira a categoria do produto(eletrônico/alimento):")
preco = float(input("Insira o preço do produto:"))

dic.update({"categoria": categoria})
dic.update({"preco": preco})

match dic:
    case _ if categoria == "eletrônico" and preco > 1000:
        print("Produto de Luxo")
    case _ if categoria == "eletrônico" and preco <= 1000:
        print("Produto Comum")
    case _ if categoria == "alimento": 
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")