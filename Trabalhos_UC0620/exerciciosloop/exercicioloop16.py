num_total = 0
num_inseridos = 0
while num_inseridos != 30:
    num = int(input("Insira 30 numeros pares entre 1 e 50 para mostrar a média: "))
    if num % 2 != 0 and (num > 50 or num < 1):
        print("Tem que ser numero par e entre 1 e 50")
    elif num > 50 or num < 1:
        print("Tem que ser entre 1 e 50")
    elif num % 2 != 0:
        print("Tem que ser par")
    else:
        num_total += num
        num_inseridos += 1
        
    


print(f"Média dos numeros: {num_total / 30}")