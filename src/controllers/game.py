from flask import Blueprint, request, make_response, render_template, abort
from src.classes.jogador import Jogador
from src.classes.jogoVelha import JogoVelha
from src.utils.checkWinner import checkWinner

gameController = Blueprint("game", __name__)

jogo = JogoVelha()

@gameController.route('/init', methods=['POST'])
def init():
    nome_jogador1 = request.form['jogador1']
    nome_jogador2 = request.form['jogador2']
    
    jogo.iniciar_jogo(nome_jogador1, nome_jogador2)
    
    response = make_response(render_template('veia.html'))

    response.set_cookie('jogadorAtual', nome_jogador1)
    
    return response

@gameController.route('/reset', methods=['POST'])
def reset():
    jogo.tabuleiro.reset()
    return 'OK'

@gameController.route('/restart', methods=['POST'])
def restart():
    response = make_response(render_template('veia.html'))
    response.set_cookie('jogadorAtual', '', expires=0)
    jogo.resetar_jogo()

    return 'OK'

@gameController.route('/setOnCeil', methods=['POST'])
def set_on_ceil():
    pos = int(request.form['pos'])
    jogadorAtual = request.form['jogadorAtual'].strip('"')

    if jogadorAtual is None or jogo.jogador1 is None or jogo.jogador2 is None:
        return { 'message': "Jogador não selecionado!" }

    if jogo.tabuleiro.tabuleiro[pos] is None:
        forma_jogador_atual = 'X' if jogadorAtual == jogo.jogador1.nome else 'O'
        jogo.tabuleiro.tabuleiro[pos] = forma_jogador_atual
        resultado = checkWinner(jogo.tabuleiro.tabuleiro)
        if resultado is None:
            proximo_jogador = jogo.jogador2.nome if jogadorAtual == jogo.jogador1.nome else jogo.jogador1.nome
            response = make_response({ 'forma': forma_jogador_atual })
            response.set_cookie('jogadorAtual', proximo_jogador)
            return response
        if resultado:
           return { 'message': f"Vencedor: {jogadorAtual}", 'forma': forma_jogador_atual }
        return { 'message': "Empate", 'forma': forma_jogador_atual }
        
    
    abort(400)
