def verificar_login_crush(login, lista_usuarios):
    for user in lista_usuarios:
        if login == user[1]:  # email
            return True
    return False



def fazer_login_usuario(email, senha, lista_usuarios):
    for usuario in lista_usuarios:
        if email == usuario[1] and senha == usuario[2]:
            return True
    return False