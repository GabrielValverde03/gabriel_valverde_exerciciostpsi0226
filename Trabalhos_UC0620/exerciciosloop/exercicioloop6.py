primos = 0
num = 2

while primos != 10:
    num+=1
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        primos +=1
    
