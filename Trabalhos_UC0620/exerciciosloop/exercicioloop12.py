num = int(input("Insira um numero:"))
operacoes = 0
for i in range (1,num+1):
    print(f"soma : {num} + {i} = {num + i}",end= " --- ")
    print(f"dividir : {num} / {i} = {num / i}",end= " --- ")
    print(f"multiplicação : {num} * {i} = {num * i}",end= " --- ")
    print(f"subtração : {num} - {i} = {num - i}")
    
    operacoes += 4
print(f"Operações realizadas:{operacoes}")