from flask import Flask, render_template, request, make_response
from utils.check_winner import check_winner
import os

app = Flask(__name__)

class Jogador:
    def __init__(self, nome, forma):
        self.nome = nome
        self.forma = forma

jogador1 = None
jogador2 = None
jogadorAtual = None
formas = ['X', 'O']
tabuleiro = [None] * 9

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/initGame', methods=['POST'])
def init_game():
    global jogador1, jogador2, jogadorAtual
    nome_jogador1 = request.form['jogador1']
    nome_jogador2 = request.form['jogador2']
    
    jogador1 = Jogador(nome_jogador1, 0)  # X
    jogador2 = Jogador(nome_jogador2, 1)  # O
    jogadorAtual = jogador1
    
    response = make_response(render_template('veia.html'))

    response.set_cookie('jogador1', nome_jogador1)
    response.set_cookie('jogador2', nome_jogador2)
    response.set_cookie('jogadorAtual', str(jogadorAtual))
    
    return response

@app.route('/reset', methods=['POST'])
def reset():
    global jogador1, jogador2, jogadorAtual, tabuleiro
    tabuleiro = [None] * 9
    return 'OK'

@app.route('/restart', methods=['POST'])
def restart():
    global jogador1, jogador2, jogadorAtual, tabuleiro

    response = make_response(render_template('veia.html'))
    response.set_cookie('jogador1', '', expires=0)
    response.set_cookie('jogador2', '', expires=0)
    response.set_cookie('jogadorAtual', '', expires=0)

    jogador1 = None
    jogador2 = None
    jogadorAtual = None
    tabuleiro = [None] * 9

    return 'OK'

@app.route('/setOnCeil', methods=['POST'])
def set_on_ceil():
    global jogadorAtual, tabuleiro
    
    if jogadorAtual is None:
        return { message: "Jogador não selecionado!" }

    pos = int(request.form['pos'])

    if tabuleiro[pos] is None:
        tabuleiro[pos] = formas[jogadorAtual.forma]
        jogadorAtual = jogador2 if jogadorAtual.forma == 0 else jogador1
        resultado = check_winner(tabuleiro)
        return formas[jogadorAtual.forma] if resultado is None else resultado

    return { message: "Célula já preenchida!", forma: formas[jogadorAtual.forma] }

if __name__ == '__main__':
    app.run(debug=True)