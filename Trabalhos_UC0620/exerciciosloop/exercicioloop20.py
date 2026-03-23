opcao = 0
while opcao != 3:

    print("\n-----------MENU-----------")
    print("1 - Verificar numero de 1 até numero escolhido(primo, divisores, perfeitos)")
    print("2 - Calculadora simples")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            num = 0
            
            while num < 1 or num > 30000:
                num = int(input("Insira um numero de 1 a 30000 para fazer a verificação: "))
            
            for i in range(1, num + 1):
                print(f"Numero: {i}")
                soma_divisores = 0
                contagem_divisores = 0
                if i == 1:
                    print("Numero não primo")
                else:            
                    for n in range(2, i):
                        if i % n == 0:
                            print("Numero não primo")
                            break
                    else:
                        print("Numero primo")
                for j in range(1, i):
                    if i % j == 0:
                        soma_divisores += j
                        contagem_divisores += 1
                print(f"Numero de divisores:{contagem_divisores}")
                if soma_divisores == i:
                    print("Numero é perfeito")
                else: 
                    print("Numero não é perfeito")
                if i % 10 == 0:
                    resposta= input("Deseja continuar?")
                    if resposta == "nao" or resposta == "não":
                        break

        case 2:
            opc_calculadora= 0
            while opc_calculadora != 6:
                print("\n-----------CALCULADORA-----------")
                print("1 - Soma")
                print("2 - Subtração")
                print("3 - Multiplicação")
                print("4 - Divisão")
                print("5 - Tabuada")
                print("6 - Voltar")
                opc_calculadora = int(input("Escolha uma opção: "))
                match opc_calculadora:                    
                    case 1:
                        resposta =""
                        while resposta != "não" and resposta != "nao":                                             
                            print("Insira 2 numeros para fazer a soma:")
                            num1 = float(input())
                            num2 = float(input())                           
                            print(f"{num1} + {num2} = {num1 + num2}")
                            resposta = input("Quer continuar?")
                    case 2:
                        resposta =""
                        while resposta != "não" and resposta != "nao":                                             
                            print("Insira 2 numeros para fazer a subtração:")
                            num1 = float(input())
                            num2 = float(input())                           
                            print(f"{num1} - {num2} = {num1 - num2}")
                            resposta = input("Quer continuar?")
                    case 3:
                        resposta =""
                        while resposta != "não" and resposta != "nao":                                             
                            print("Insira 2 numeros para fazer a multiplicação:")
                            num1 = float(input())
                            num2 = float(input())                           
                            print(f"{num1} * {num2} = {num1 * num2}")
                            resposta = input("Quer continuar?")     
                    case 4:
                        resposta =""
                        while resposta != "não" and resposta != "nao":                                             
                            print("Insira 2 numeros para fazer a divisão:")
                            num1 = float(input())
                            num2 = float(input())                           
                            print(f"{num1} / {num2} = {num1 / num2}")
                            resposta = input("Quer continuar?") 
                    case 5:
                        num = 0
                        while num < 1 or num > 1000: 
                            num = int(input("Insira um numero para fazer a tabuada(entre 1 e 1000):"))
                            if num < 1 or num > 1000:
                                print("Tem que ser entre 1 e 1000")
                        num_tabuada = 0
                        while num_tabuada < 1 or num_tabuada > 1000: 
                            num_tabuada = int(input(("Até que numero quer fazer a sua tabuada(entre 1 e 1000):")))
                            if num_tabuada < 1 or num_tabuada > 1000:
                                print("Tem que ser entre 1 e 1000")
                        for i in range(1, num_tabuada + 1):
                            print(f"{num} * {i} = {num*i}")
                            if i % 20 == 0:
                                resposta= input("Deseja continuar?")
                                if resposta == "nao" or resposta == "não":
                                    break
                        break
                    case 6:
                        break
        case 3:
            break                 
