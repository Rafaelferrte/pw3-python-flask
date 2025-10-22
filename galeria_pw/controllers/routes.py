from flask import render_template, request, url_for, redirect, flash, session
from models.database import db, Usuario, Imagem
import os
import uuid

from werkzeug.security import generate_password_hash, check_password_hash

def init_app(app):
    # Implementando o MIDDLEWARE para checagem da autenticação
    @app.before_request
    def check_auth():
        # Rotas que não precisam de autenticação
        routes = ['home', 'login', 'caduser']
        # Se a rota atual não requerer autenticação, o sistema permite o acesso
        if request.endpoint in routes or request.path.startswith('/static/'):
            return
        # Se o usuario não estiver autenticado, redireciona para a página de login
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
    @app.route('/')
    def home():
        return render_template('login.html')
    
    @app.route('/index')
    def index():
        imagens = Imagem.query.all()
        return render_template('index.html', imagens=imagens)
    
    # ROTA de LOGIN
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            user = Usuario.query.filter_by(email=email).first()
            if user and check_password_hash(user.senha, senha):
                # Criando a sessão para o usuário
                session['user_id'] = user.id
                session['email'] = user.email
                flash(f'Login realizado com sucesso! Bem-vindo {user.nome}!', 'success')
                return redirect(url_for('index'))
            
            else:
                flash("Falha no login! Verifique o nome de usuário e senha e tente novamente.", "danger")
                return redirect(url_for('login'))
        return render_template('login.html')
    
    
    # ROTA de LOGOUT
    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        session.clear()
        flash("Você foi desconectado!", "warning")
        return redirect(url_for('home'))
    
    # ROTA de CADASTRO
    @app.route('/caduser', methods=['GET', 'POST'])
    def caduser():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']

            user = Usuario.query.filter_by(email=email).first()
            if user:
                flash("Usuário já cadastrado! Faça o login", "danger")
                return redirect(url_for('caduser'))
            else:
                hashed_password = generate_password_hash(senha, method='scrypt')
                new_user = Usuario(nome=nome, email=email, senha=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash("Cadastro realizado com sucesso! Faça o login.", "success")
                return redirect(url_for('login'))
        return render_template('caduser.html')
    
    # Definindo tipos de arquivos permitidos
    FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])
    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES

    # UPLOAD DE IMAGENS
    @app.route('/galeria', methods=['GET', 'POST'])
    def galeria():
        imagens = Imagem.query.all()
        
        if request.method == 'POST':
            file = request.files['file']

            if not arquivos_permitidos(file.filename):
                flash("Utilize apenas arquivos de imagem (png, jpg, jpeg, gif).", 'danger')
                return redirect(request.url)
            
            ext = file.filename.rsplit('.', 1)[1].lower()
            filename = f"{uuid.uuid4()}.{ext}"

            # Grava no banco
            img = Imagem(filename=filename)
            db.session.add(img)
            db.session.commit()

            # Salva no diretório de uploads
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash("Imagem enviada com sucesso!", 'success')
            return redirect(url_for('index'))  # volta ao index para ver as imagens

        return render_template('galeria.html', imagens=imagens)
    
    @app.route('/sobre')
    def sobre():
        return render_template('index.html')