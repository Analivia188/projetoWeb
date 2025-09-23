from flask import *

app = Flask(__name__)

usuarios = [
    ["Ana Livia", "ana@example.com", "123456"],
    ["Cindy", "cindy@leroo.com", "1234567"],
]

@app.route('/')
def pag_principal():
    return render_template('tela_inicial.html')

@app.route('/Cadastrar_Usuario', methods=['GET', 'POST'])
def Cadastrar_Usuario():
    global usuarios
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        for usuario in usuarios:
            if usuario[1] == email:
                msg = "Usuário já existe!"
                return render_template('Cadastro.html', msg=msg)

        usuarios.append([nome, email, senha])
        msg = nome + " foi cadastrado(a) com sucesso!"
        return render_template('Loja.html', msg=msg)

    return render_template('Cadastro.html')

@app.route('/Fazer_Login', methods=["GET", "POST"])
def Fazer_Login():
    msg = ""
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        for usuario in usuarios:
            if usuario[1] == email and usuario[2] == senha:
                return render_template("Loja.html")
        msg = "Email ou senha incorretos"
    return render_template("Login.html", msg=msg)


@app.route('/Verificar_Senha', methods=['GET', 'POST'])
def administrador():
    if request.method == 'GET':
        return render_template('Verificar_ADM.html')
    else:
        senha = request.form.get('senha')
        if senha == '1234':
            return render_template('Aba_do_admin.html')
        else:
            msg = "Senha incorreta, tente novamente!"
            return render_template('Verificar_ADM.html', msg=msg)

@app.route('/Remover_Usuario', methods=['post'])
def remover_usuario():
    global usuarios
    email = request.form.get('email')
    existe = False
    indice = 0
    for usuario in usuarios:
        if usuario[1] == email:
            existe = True
            break
        indice += 1

    if existe:
        usuarios.pop(indice)
    else:
        print('Não consta na lista de usuarios')

    return render_template('Aba_do_admin.html')

@app.route('/Listar_Usuarios', methods=['get'])
def listar_usuarios():
    global usuarios
    if len(usuarios) > 0:
        enviar = []
        for u in usuarios:
            enviar.append(u[0])
        return render_template('Listar_Usuarios.html', lista=enviar)

@app.route('/quiz1')
def quiz1():
    return render_template("Quiz1.html")

if __name__ == '__main__':
    app.run()