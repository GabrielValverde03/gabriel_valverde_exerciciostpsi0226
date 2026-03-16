dic = {"metodo": "","conteudo": ""}

metodo = input("Insira metodo(GET/POST):")
conteudo = input("Insira o conteudo:")

dic.update({"metodo": metodo})
dic.update({"conteudo": conteudo})

match dic:
    case _ if metodo == "GET":
        print("Requisição GET recebida")
    case _ if metodo == "POST" and conteudo == "":
        print("Requisição POST sem dados")
    case _ if metodo == "POST" and conteudo != "":
        print("Requisição POST com dados válidos")
    case _:
        print("Método não suportado")