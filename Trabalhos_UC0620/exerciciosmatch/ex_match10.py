jogada1 = input("Jogador 1 pedra papel ou tesoura:")
jogada2 = input("Jogador 2 pedra papel ou tesoura:")

match (jogada1, jogada2):
    case _ if jogada1 == jogada2:
        print("Empate")
    case("pedra", "tesoura") | ("papel", "pedra") | ("tesoura", "papel"):
        print("Jogador 1 ganhou")
    case("pedra", "papel") | ("papel", "tesoura") | ("tesoura", "pedra"):
        print("Jogador 2 ganhou")
    case _:
        print("Jogadas inválidas")
    
        