from flask import *
from utils.auxiliares import *

app = Flask(__name__)

app.secret_key = 'segredo'

usuarios = [["Ana Livia", "ana@example.com", "123456"],["Cindy", "cindy@leroo.com", "1234567"],]

@app.route('/')
def pag_principal():
    return render_template('tela_inicial.html')

@app.route('/Cadastrar_Usuario', methods=['GET', 'POST'])
def Cadastrar_Usuario():
    global usuarios
    if request.method == 'GET':
        return render_template('Cadastro.html')
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    if fazer_login_usuario(email, senha, usuarios):
        msg = "Usuário já existe!"
        return render_template('Cadastro.html', msg=msg)

    usuarios.append([nome, email, senha])
    msg = nome + " foi cadastrado(a) com sucesso!"
    return render_template('Loja.html', msg=msg)


@app.route('/Fazer_Login', methods=["GET", "POST"])
def Fazer_Login():
    if request.method == "GET":
        return render_template("Login.html")

    email = request.form.get("email")
    senha = request.form.get("senha")

    if fazer_login_usuario(email, senha, usuarios):
        session['usuario'] = email
        return render_template("Loja.html")

    msg = "Email ou senha incorretos"
    return render_template("Login.html", msg=msg)


@app.route('/Verificar_Senha', methods=['GET', 'POST'])
def administrador():
    if request.method == 'GET':
        return render_template('Verificar_ADM.html')
    else:
        login = request.form.get('login')
        senha = request.form.get('senha')
        if login == 'me' and senha == '321':
            session['login'] = login
            return render_template('Aba_do_admin.html')
        else:
            return render_template('tela_inicial.html',)

@app.route('/administrador')
def admin():
    return render_template('Aba_do_admin.html')

@app.route('/Eliminar', methods=['GET', 'POST'])
def remover_usuario():
    global usuarios
    if 'login' not in session or session['login'] != 'me':
        return render_template('tela_inicial.htm')

    if request.method == 'POST':
        email = request.form.get('email')
        existe = False
        indice = 0
        for usuario in usuarios:
            if usuario[1] == email:
                existe = True
                break
                indice += 1
                return render_template('Remover.html')
        if existe:
            usuarios.pop(indice)
        else:
            print('Não consta na lista de usuarios')

    return render_template('Remover.html')

@app.route('/Listar_Usuarios', methods=['GET'])
def listar_usuarios():
    if 'login' in session and session['login'] == 'me':
        if len(usuarios) > 0:
            return render_template('Listar_Usuarios.html', lista=usuarios)
        else:
            return render_template('Listar_Usuarios.html')

@app.route('/detalhes')
def mostrar_detalhes():
    email = request.values.get('email')
    achei = None
    for user in usuarios:
        if email == user[1]:
            achei = user
            break
    return render_template('Detalhes_usuario.html', usuarios=achei)

@app.route('/Cadastrar_produto')


@app.route('/quiz1')
def quiz1():
    return render_template("Quiz1.html")

if __name__ == '__main__':
    app.run()