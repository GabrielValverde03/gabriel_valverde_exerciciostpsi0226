print("Codigo ASCII e codigo correspondente:")

num_as = 0
for i in range(0,256):
    print(f"{num_as}:{chr(num_as)}")
    num_as += 1
    if num_as % 20 == 0:
        resposta = input("Quer continuar? ")
        if resposta == "não" or resposta == "nao":
            break


