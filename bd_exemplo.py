import sqlite3

conexao = sqlite3.connect("meu_banco.db")

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    '''
)

# cursor.execute(
#     '''
#         INSERT INTO usuarios(nome, email) VALUES (?, ?);
#     '''
#     , ("Luiz Gustavo", "gustavo_veras@ifsp.edu.br")
# )

# cursor.execute(
#     '''
#         INSERT INTO usuarios(nome, email) VALUES (?, ?);
#     '''
#     , ("Ana Paula", "ana_paula@ifsp.edu.br")
# )

cursor.execute(
    '''
        SELECT * FROM usuarios WHERE id = ?;
    '''
    , (1, )
)

# Retorna tdos os resultados do SELECT anterior como lista no Python
# [
#     1: [1: id, 2: nome, 3: email]
#     2: [1: id, 2: nome, 3: email]
#     ...
# ]
# usuarios = cursor.fetchall()

# retorna uma lista com os dados de uma única linha
# [
#     1: id,
#     2: nome,
#     3: email
# ]
usuario = cursor.fetchone()

print(f"Id: {usuario[0]} - Nome: {usuario[1]} - Email:{usuario[2]}")

# for u in usuarios:
#     print(f"Id: {u[0]} - Nome: {u[1]} - Email:{u[2]}")

cursor.execute(
    '''
        UPDATE usuarios 
        SET email = ?
        WHERE id = ?;
    '''
    , ("luiz_gustavo@ifsp.edu.br", 1)
)

cursor.execute(
    '''
        DELETE FROM usuarios
        WHERE id = ?;
    '''
    , (2, )
)

conexao.commit() ##  aplica o SQL ao banco
conexao.close()

print("Conexão com banco estabelecida")
