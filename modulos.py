import json

def save(list, path):
    data = []
    with open(path, 'w', encoding='utf-8') as file:
        data = json.dump(
            list,
            file,
            ensure_ascii=False,
            indent=2
        )
    return data


def read(list, path):
    data = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        return  save(list, path)
    return data

def verificar(entry_user, entry_senha, entry_confirma_senha, list_users, sign_up_erro_nome, sign_up_erro_senha, cadastrar, sign_up_cadastro_feito ):
        user = entry_user.get()
        senha = entry_senha.get()
        senha_confirmada = entry_confirma_senha.get()
        user_negado = False

        if list_users == []:
            pass
        else:
            for usuario in list_users:
                if usuario['username'] == user:
                    user_negado = True

        if user_negado:
            sign_up_erro_nome()
        elif senha != senha_confirmada:
            sign_up_erro_senha()
        else:
            cadastrar()
            sign_up_cadastro_feito()


