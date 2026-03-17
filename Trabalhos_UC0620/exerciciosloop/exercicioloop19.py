bonatchi = 0
num1 = 0
num2 = 1
num3 = 0
while True:
    if bonatchi < 60:
        print(num2,end=", ")
        num3 = num2
        num2 = num1 + num2
        num1 = num3
        bonatchi +=1
    else:
        break
        

