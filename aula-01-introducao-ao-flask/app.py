# Importando o Flask
from flask import Flask, render_template

# Carregando o Flask na variavel app
app = Flask(__name__, template_folder='views')

# Criando a primeira rota do site
@app.route('/')
# Criando função no Python
def home():
    return render_template('index.html')

#Rota de games
@app.route('/games')
def games():
    # Dicionario em Python (Objeto)
    game = {
        'Titulo': 'CS-GO',
        'Ano': 2012,
        'Categoria': 'FPS Online'
    }
    jogadores = ['Miguel José', 'Miguel Isack', 'Leaf', 'Quemario', 'Trop', 'Aspax', 'maxxdiego']
    jogos= ['EA Sports 2025', 'Cuphead', 'Doom Eternal', 'Minecraft', 'Fallout 4']
    return render_template('games.html',
                           game=game,
                           jogadores=jogadores,
                           jogos=jogos)

# Iniciando o servidor no localhost, porta 5000, modo de depuração ativado
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)     