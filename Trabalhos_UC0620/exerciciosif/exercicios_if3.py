num1=int(input("Insira um valor:"))
num2=int(input("Insira outro valor:"))

if num1 > num2:
    print(f"Crescente:{num2}, {num1}")
    print(f"Decrescente:{num1}, {num2}")
else:
    print(f"Crescente:{num1}, {num2}")
    print(f"Decrescente:{num2}, {num1}")