import sqlite3
import bcrypt

def fazer_login(usuario, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    # Prepared statement: placeholders (?) impedem SQL Injection
    query = "SELECT password FROM usuarios WHERE username = ?"
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado and bcrypt.checkpw(senha.encode(), resultado[0]):
        return "Acesso Permitido!"
    else:
        return "Acesso Negado."


def cadastrar_usuario(usuario, senha):
    """Helper: cadastra usuário com senha hasheada (bcrypt)."""
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (usuario, hash_senha))
    conexao.commit()
    conexao.close()
