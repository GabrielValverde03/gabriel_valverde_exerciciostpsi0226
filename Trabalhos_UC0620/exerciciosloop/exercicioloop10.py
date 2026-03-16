num = int(input("Insira um numero:"))

numdivisores = 0

for i in range(1, num+1):
    if num % i == 0:
        numdivisores += 1

print(numdivisores)