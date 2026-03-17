
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
            if soma_divisores == i:
                print("Numero é perfeito")
            else: 
                print("Numero não é perfeito")
            if i % 10 == 0:
                resposta= input("Deseja continuar?")
                if resposta == "nao" or resposta == "não":
                    break
            


