from flask import *
from dao.banco import init_db, Session
from dao.usuarioDAO import *
from dao.produtoDAO import ProdutoDAO
from modelos.modelos import Produto

app = Flask(__name__)
app.secret_key = 'segredo'

@app.before_request
def pegar_sessao():
    g.session = Session()

@app.teardown_appcontext
def encerrar_sessao(exception=None):
    Session.remove()

@app.route('/')
def pag_principal():
    return render_template('tela_inicial.html')

@app.route('/Cadastrar_Usuario', methods=['GET', 'POST'])
def Cadastrar_Usuario():
    if request.method == 'GET':
        return render_template('Cliente/Cadastro.html')

    usuario_dao = UsuarioDAO(g.session)

    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirma = request.form.get('confirmacao')

    if usuario_dao.buscar_por_email(email):
        msg = 'Este email já está cadastrado'
        return render_template('Cliente/Cadastro.html', msg=msg)

    if senha == confirma:
        novo_usuario = Usuario(email=email, nome=nome, senha=senha)
        usuario_dao.criar(novo_usuario)
        msg = "Usuário cadastrado com sucesso!"
        return render_template('Cliente/Login.html', msg=msg)

    if usuario_dao.buscar_por_email(email):
        return render_template(
            'Cliente/Cadastro.html',
            msg='Este email já está cadastrado'
        )

    else:
        msg = 'A senha e a confirmação de senha não são iguais'
        return render_template('Cliente/Cadastro.html', msg=msg)

@app.route('/Fazer_Login', methods=["GET", "POST"])
def Fazer_Login():
    if request.method == 'GET' and 'login' in session:
        return render_template('Cliente/Loja.html')

    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario_dao = UsuarioDAO(g.session)

    #if verificar_login(usuarios, login, senha):
    usuario = usuario_dao.autenticar(email, senha)
    if usuario:
        print(usuario)
        session['login'] = email
        return render_template('Cliente/Loja.html')
    else:
        #aqui o usuario digitou o login ou senha errado
        msg = 'Email ou senha incorretos'
        return render_template('Cliente/Login.html', msg=msg)

@app.route('/Verificar_Senha', methods=['GET', 'POST'])
def administrador():
    if request.method == 'GET':
        return render_template('Administrador/Verificar_ADM.html')
    else:
        login = request.form.get('login')
        senha = request.form.get('senha')
        if login == 'me' and senha == '321':
            session['login'] = login
            return render_template('Administrador/Aba_do_admin.html')

        return render_template('tela_inicial.html',)


@app.route('/Listar_Usuarios', methods=['GET'])
def listar_usuarios():
    if 'login' in session:
        usuarioDAO = UsuarioDAO(g.session)
        usuarios_lista = usuarioDAO.listar_usuarios()
        print("USUÁRIOS:", usuarios_lista)
        return render_template('Administrador/Listar_Usuarios.html',lista=usuarios_lista)
    else:
        return render_template('Administrador/Listar_Usuarios.html')

@app.route('/detalhes')
def mostrar_detalhes():
    email = request.values.get('email')
    usuario_dao = UsuarioDAO(g.session)
    usuario = usuario_dao.buscar_por_email(email)
    if not usuario:
        return "Usuário não encontrado"

    return render_template('Administrador/detalhes.html',usuario=usuario)

@app.route('/quiz1')
def quiz1():
    return render_template("Cliente/Quiz1.html")

@app.route('/carrinho')
def carrinho():
    return render_template("Cliente/Carrinho.html")


@app.route('/Cadastrar_Produto', methods=['GET', 'POST'])
def cadastrar_produto():
    if 'login' not in session:
        return render_template('tela_inicial.html')

    if request.method == 'GET':
        return render_template('Administrador/Produto/Cadastro_Produto.html')

    nome = request.form.get('nome')
    valor = request.form.get('valor')
    produto_dao = ProdutoDAO(g.session)
    novo_produto = Produto(
        nome=nome,
        valor=float(valor)
    )
    produto_dao.criar(novo_produto)
    msg = 'Produto cadastrado com sucesso!'
    return render_template('Administrador/Aba_do_admin.html', msg=msg)


@app.route('/Listar_Produtos')
def listar_meus_produtos():
    if 'login' not in session:
        return render_template('tela_inicial.html')

    produto_dao = ProdutoDAO(g.session)
    produtos = produto_dao.listar_todos()

    return render_template('Administrador/Produto/Listar_Produtos.html',lista=produtos)

@app.route('/logout')
def fazer_logout():
    session.clear()
    return render_template('Cliente/Login.html')

if __name__ == '__main__':
    init_db()
    app.run()