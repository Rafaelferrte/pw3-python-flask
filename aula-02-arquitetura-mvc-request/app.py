# Importando o Flask
from flask import Flask, render_template
# Importando as rotas que estão nos controllers
from controllers import routes


# Carregando o Flask na variavel app
app = Flask(__name__, template_folder='views')

# Chamando as rotas
routes.init_app(app)

# Iniciando o servidor no localhost, porta 5000, modo de depuração ativado
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)     