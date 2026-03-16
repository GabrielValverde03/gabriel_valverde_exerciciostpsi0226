pares = 0
impares = 0

for n in range(10):
    nums = int(input("Digite um numero: "))

    if nums % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Pares:", pares, sep="")
print("Impares:", impares, sep="")
