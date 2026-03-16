dic = {"status": "","tempo_resposta": 0}

status = input("Insira o status do servidor(ok/erro):")
tempo_resposta = int(input("Insira tempo de resposta:"))

dic.update({"status": status})
dic.update({"tempo_resposta": tempo_resposta})

match dic:
    case _ if status == "ok" and tempo_resposta <= 200:
        print("Servidor ativo")
    case _ if status == "ok" and tempo_resposta > 200:
        print("Servidor lento")
    case _ if status == "erro": 
        print("Servidor indisponivel")
    case _:
        print("Estado desconhecido")