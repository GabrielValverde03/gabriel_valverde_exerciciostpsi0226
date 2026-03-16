num = int(input("Insira um numero para fazer a tabuada: "))

print(f"Tabuada de {num}:")
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")