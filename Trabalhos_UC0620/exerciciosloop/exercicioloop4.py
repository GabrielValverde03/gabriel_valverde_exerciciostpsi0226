num = int(input("Insira um numero:"))

for i in range(2, num):
    if num % i == 0:
        print("numero não primo")
        break
else:
    print("numero primo")