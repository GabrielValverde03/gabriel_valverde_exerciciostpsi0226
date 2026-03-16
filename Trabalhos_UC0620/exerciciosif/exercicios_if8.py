nota1 = int(input("Primeiro aluno:"))
nota2 = int(input("Segundo aluno:"))
nota3 = int(input("Terceiro aluno:"))
nota4 = int(input("Quarto aluno:"))
nota5 = int(input("Quinto aluno"))
nota6 = int(input("Sexto aluno:"))
nota7 = int(input("Setimo aluno:"))
nota8 = int(input("Oitavo aluno:"))
nota9 = int(input("Nono aluno:"))
nota10 = int(input("Decimo aluno:"))

nota_igual_acima = 0

media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 +nota9 +nota10) /10
print(f"Média dos 10 alunos:{media}")

if nota1 >= media:
    nota_igual_acima += 1
if nota2 >= media:
    nota_igual_acima += 1
if nota3 >= media:
    nota_igual_acima += 1
if nota4 >= media:
    nota_igual_acima += 1
if nota5 >= media:
    nota_igual_acima += 1
if nota6 >= media:
    nota_igual_acima += 1
if nota7 >= media:
    nota_igual_acima += 1
if nota8 >= media:
    nota_igual_acima += 1
if nota9 >= media:
    nota_igual_acima += 1     
if nota10 >= media:
    nota_igual_acima += 1 

print("Notas acima da média:", nota_igual_acima)     

