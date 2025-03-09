import customtkinter as ctk

from modulos import *

app = ctk.CTk()
app.title("Login de Usuário")
app.geometry("600x400")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

canvas = ctk.CTkCanvas(app)
scrollbar = ctk.CTkScrollbar(app, command=canvas.yview)

ctk.set_appearance_mode("dark")


def update_page():
    for widget in app.winfo_children():
        widget.pack_forget()


CAMINHO_USERS = "users.json"
list_users = read([], CAMINHO_USERS)


def home_page():
    update_page()

    def verificar_login():
        user = campo_username.get()
        senha = campo_senha.get()
        user_a_validar = ""
        user_espacos = campo_username.get().strip()
        senha_espacos = campo_senha.get().strip()

        if list_users == []:
            ...
        else:
            for usuario in list_users:
                if usuario["username"] == user:
                    user_a_validar = usuario

        if not user_espacos or not senha_espacos:
            login_resultado.configure(text="Preencha todos os campos", text_color="red")

        elif user_a_validar == "":
            login_resultado.configure(text="Usuário não encontrado", text_color="red")

        elif user_a_validar["username"] == user and user_a_validar["senha"] == senha:
            login_resultado.configure(
                text="Login feito com sucesso", text_color="green"
            )
        else:
            login_resultado.configure(text="Login incorreto", text_color="red")

    label_usuário = ctk.CTkLabel(app, text="Usuário", font=("Arial", 14, "bold"))
    label_usuário.pack(pady=10, expand=True)  # adicionando a aplicação

    campo_username = ctk.CTkEntry(app, placeholder_text="Digite seu username")
    campo_username.pack(pady=3, expand=True)

    label_senha = ctk.CTkLabel(app, text="Senha", font=("Arial", 14, "bold"))
    label_senha.pack(pady=10, expand=True)  # adicionando a aplicação

    campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*")
    campo_senha.pack(pady=3, expand=True)

    button_login = ctk.CTkButton(app, text="Login", command=verificar_login)
    button_login.pack(pady=20, expand=True)

    button_sign_up = ctk.CTkButton(app, text="Cadastrar", command=sign_up)
    button_sign_up.pack(pady=1, expand=True)

    login_resultado = ctk.CTkLabel(app, text="")
    login_resultado.pack(pady=10, expand=True)


def sign_up():
    update_page()

    def cadastrar():
        user = entry_user.get()
        senha = entry_senha.get()
        dict_new_user = {"username": user, "senha": senha}
        list_users.append(dict_new_user)
        save(list_users, CAMINHO_USERS)

    def verificar():
        user = entry_user.get()
        senha = entry_senha.get()
        senha_confirmada = entry_confirma_senha.get()
        user_espaco = entry_user.get().strip()
        senha_espaco = entry_senha.get().strip()
        senha_confirma_espaco = entry_confirma_senha.get().strip()
        user_negado = False

        if list_users == []:
            pass
        else:
            for usuario in list_users:
                if usuario["username"] == user:
                    user_negado = True

        if not user_espaco or not senha_espaco or not senha_confirma_espaco:
            label_cadastro.configure(text="Preencha todos os campos", text_color="red")

        elif user_negado:
            label_cadastro.configure(
                text="Este nome de usuário já existe, tente outro", text_color="red"
            )

        elif senha != senha_confirmada:
            label_cadastro.configure(
                text="As senhas inseridas não são iguais", text_color="red"
            )
        else:
            cadastrar()
            label_cadastro.configure(
                text="Cadastro feito com sucesso", text_color="green"
            )

    label_criar_user = ctk.CTkLabel(
        app, text="Crie um nome de usuário", font=("Arial", 14, "bold")
    )
    label_criar_user.pack(pady=10)

    entry_user = ctk.CTkEntry(app, placeholder_text="Nome de usuário")
    entry_user.pack(pady=3)

    label_criar_senha = ctk.CTkLabel(
        app, text="Crie uma senha", font=("Arial", 14, "bold")
    )
    label_criar_senha.pack(pady=10)

    entry_senha = ctk.CTkEntry(app, placeholder_text="Senha", show="*")
    entry_senha.pack(pady=3)

    label_confirma_senha = ctk.CTkLabel(
        app, text="Confirme sua senha", font=("Arial", 14, "bold")
    )
    label_confirma_senha.pack(pady=10)

    entry_confirma_senha = ctk.CTkEntry(
        app, placeholder_text="Confirmar senha", show="*"
    )
    entry_confirma_senha.pack(pady=3)

    button_cadastro = ctk.CTkButton(app, text="Cadastrar usuário", command=verificar)
    button_cadastro.pack(pady=20)

    button_back = ctk.CTkButton(app, text="Voltar", command=home_page)
    button_back.pack(pady=3)

    label_cadastro = ctk.CTkLabel(app, text="")
    label_cadastro.pack(pady=10)


home_page()
app.mainloop()
