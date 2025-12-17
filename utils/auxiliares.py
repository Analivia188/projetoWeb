def verificar_login(lista, email, senha):
    for usuario in lista:
        if usuario[1] == email and usuario[2] == senha:
            return True

    return False


def buscar_usuario(lista, email):
    for usuario in lista:
        if usuario[1] == email:
            return usuario

    return None