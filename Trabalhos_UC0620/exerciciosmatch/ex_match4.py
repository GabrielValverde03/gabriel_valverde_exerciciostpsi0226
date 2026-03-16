valor = input("Digite um valor:")

match valor:
    case valor if type(valor) == str:
        print("String textual")
    case valor if type(valor) == int:
        print("Numero inteiro")
    case valor if type(valor) == float:
        print("Numero Decimal")
    case valor if valor.startswith("[]"):
        print("Lista")
    case _:
        print("Tipo desconhecido")