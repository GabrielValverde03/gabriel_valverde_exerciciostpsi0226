opcao = input("Escolha uma operacao para efetuar(soma/subtrai/multiplica/divide):")
num1 = int(input("Insira um numero:"))
num2 = int(input("Insira outro numero:"))

match opcao:
    case "soma":
        print(num1 + num2)
    case "subtrai":
        print(num1 - num2)
    case "multiplica":
        print(num1 * num2)
    case "divide":
        print(num1 / num2)
    case _:
        print("Operação desconhecida")