val1=int(input("Insira o valor 1:"))
val2=int(input("Insira o valor 2:"))
val3=int(input("Insira o valor 3:"))

if val1>val2 and val2>val3:
    print(f"Maior: {val1}") 
    print(f"Menor: {val3}")
elif val2>val1 and val1>val3:
    print(f"Maior: {val2}") 
    print(f"Menor: {val3}")
elif val2>val3 and val3>val1:
    print(f"Maior: {val2}") 
    print(f"Menor: {val1}")
elif val3>val2 and val2>val1:
    print(f"Maior: {val3}") 
    print(f"Menor: {val1}")
elif val3>val1 and val1>val2:
    print(f"Maior: {val3}") 
    print(f"Menor: {val2}")
else:
    print(f"Maior: {val1}") 
    print(f"Menor: {val2}")



