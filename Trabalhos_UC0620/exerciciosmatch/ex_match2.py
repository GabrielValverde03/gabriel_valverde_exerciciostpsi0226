nota = int(input("Insira uma nota (0-100): "))

match nota:
    case nota if 90 <= nota <= 100:
        print("Excelente")
    case nota if 70 <= nota <= 89:
        print("Bom")
    case nota if 50 <= nota <= 69:
        print("Suficiente")
    case nota if 0 <= nota < 50:
        print("Insuficiente")
    case _:
        print("Nota inválida")