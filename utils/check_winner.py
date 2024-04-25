def check_winner(tabuleiro):
    # Define todas as possíveis combinações de vitória
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]

    for condition in win_conditions:
        a, b, c = condition
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] and tabuleiro[a] is not None:
            return True
            
    if None not in tabuleiro:
        return False

    return None
