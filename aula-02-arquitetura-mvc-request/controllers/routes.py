from flask import render_template, request, redirect, url_for

jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']

# Dicionario em Python (Objeto)
gamelist = [{
    'Titulo': 'CS-GO',
    'Ano': 2012,
    'Categoria': 'FPS Online'
}]

consolelist = [{
    'Nome': 'Playstation 5',
    'Fabricante': 'Sony',
    'Ano': 2013,
    'Preço': 2000
}]


def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no Python
    def home():
        return render_template('index.html')

    # Rota de games
    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]

        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # Verificar se o campo 'jogador' existe
            if request.form.get('jogador'):
                # O append adiciona o item à lista
                jogadores.append(request.form.get('jogador'))
            return redirect(url_for('games'))

        jogos = ['EA Sports 2025', 'Cuphead',
                 'Doom Eternal', 'Minecraft', 'Fallout 4']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)
    # Rota de cdastro de jogos (em dicionario)

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Titulo': request.form.get('titulo'), 'Ano': request.form.get(
                    'ano'), 'Categoria': request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               gamelist=gamelist)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('fabricante') and request.form.get('ano') and request.form.get('preco'):
                consolelist.append({'Nome': request.form.get('nome'), 'Fabricante': request.form.get(
                    'fabricante'), 'Ano': request.form.get('ano'), 'Preço': request.form.get('preco')})
            return redirect(url_for('consoles'))
        return render_template('consoles.html',
                               consolelist=consolelist)
