mensagem =input("Digite uma mensagem:")

match mensagem:
    case "olá" | "bom dia":
        print("Saudação")
    case pergunta if mensagem.endswith("?"):
        print("Pergunta")
    case despedida if "tchau" or "adeus" in mensagem:
        print("Despedida")
    case _:
        print("Mensagem genérica")