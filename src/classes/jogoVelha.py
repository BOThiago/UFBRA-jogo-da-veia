from src.classes.tabuleiro import Tabuleiro
from src.classes.jogador import Jogador

class JogoVelha:
    def __init__(self):
        self.jogador1 = None
        self.jogador2 = None
        self.tabuleiro = Tabuleiro()

    def iniciar_jogo(self, nome_jogador1, nome_jogador2):
        self.jogador1 = Jogador(nome_jogador1, 0)  # X
        self.jogador2 = Jogador(nome_jogador2, 1)  # O

    def resetar_jogo(self):
        self.tabuleiro.reset()
        self.jogador1 = None
        self.jogador2 = None
