from flask import render_template, request

jogadores = ['Miguel José', 'Miguel Isack', 'Leaf', 'Quemario', 'Trop', 'Aspax', 'maxxdiego']

def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no Python
    def home():
        return render_template('index.html')

    #Rota de games
    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # Dicionario em Python (Objeto)
        game = {
            'Titulo': 'CS-GO',
            'Ano': 2012,
            'Categoria': 'FPS Online'
        }
        
        
        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # Verificar se o campo 'jogador' existe
            if request.form.get('jogador'):
                # O append adiciona o item à lista
                jogadores.append(request.form.get('jogador'))
        
        jogos= ['EA Sports 2025', 'Cuphead', 'Doom Eternal', 'Minecraft', 'Fallout 4']
        return render_template('games.html',
                            game=game,
                            jogadores=jogadores,
                            jogos=jogos)