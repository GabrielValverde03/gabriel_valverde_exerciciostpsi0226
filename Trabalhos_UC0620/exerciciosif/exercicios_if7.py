nota1 = int(input("Insira a sua primeira nota:"))
nota2 = int(input("Insira a sua segunda nota:"))
nota3 = int(input("Insira a sua terceira nota:"))

media = (nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5)


if media >= 6:
    print(f"Média: {media}")
    print("Aprovado")
else:
    print(f"Média: {media}")
    print("Reprovado")