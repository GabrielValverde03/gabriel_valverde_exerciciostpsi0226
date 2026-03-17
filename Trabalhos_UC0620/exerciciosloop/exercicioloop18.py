num = int(input("Insira um numero limite: "))

for i in range(1, num+1):
    soma_divisores = 0
    for n in range(1, i):
        if i % n == 0:
            soma_divisores += n
    if soma_divisores == i:
        print(f"O numero {i} é um numero perfeito")