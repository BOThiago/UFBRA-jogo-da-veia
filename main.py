from flask import Flask, render_template, request, make_response, abort
from utils.check_winner import check_winner

app = Flask(__name__)

class Jogador:
    def __init__(self, nome, forma):
        self.nome = nome
        self.forma = forma

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [None] * 9

    def reset(self):
        self.tabuleiro = [None] * 9

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

jogo = JogoVelha()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/initGame', methods=['POST'])
def init_game():
    nome_jogador1 = request.form['jogador1']
    nome_jogador2 = request.form['jogador2']
    
    jogo.iniciar_jogo(nome_jogador1, nome_jogador2)
    
    response = make_response(render_template('veia.html'))

    response.set_cookie('jogadorAtual', nome_jogador1)
    
    return response

@app.route('/reset', methods=['POST'])
def reset():
    jogo.tabuleiro.reset()
    return 'OK'

@app.route('/restart', methods=['POST'])
def restart():
    response = make_response(render_template('veia.html'))
    response.set_cookie('jogadorAtual', '', expires=0)
    jogo.resetar_jogo()

    return 'OK'

@app.route('/setOnCeil', methods=['POST'])
def set_on_ceil():
    pos = int(request.form['pos'])
    jogadorAtual = request.form['jogadorAtual'].strip('"')

    if jogadorAtual is None or jogo.jogador1 is None or jogo.jogador2 is None:
        return { 'message': "Jogador não selecionado!" }

    if jogo.tabuleiro.tabuleiro[pos] is None:
        forma_jogador_atual = 'X' if jogadorAtual == jogo.jogador1.nome else 'O'
        jogo.tabuleiro.tabuleiro[pos] = forma_jogador_atual
        resultado = check_winner(jogo.tabuleiro.tabuleiro)
        if resultado is None:
            proximo_jogador = jogo.jogador2.nome if jogadorAtual == jogo.jogador1.nome else jogo.jogador1.nome
            response = make_response({ 'forma': forma_jogador_atual })
            response.set_cookie('jogadorAtual', proximo_jogador)
            return response
        if resultado:
           return { 'message': f"Vencedor: {jogadorAtual}", 'forma': forma_jogador_atual }
        return { 'message': "Empate", 'forma': forma_jogador_atual }
        
    
    abort(400)

if __name__ == '__main__':
    app.run(debug=True)