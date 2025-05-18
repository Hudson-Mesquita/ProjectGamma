import sqlite3

import sqlite3

def conectar():
    conn = sqlite3.connect('gastos.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela():
    conn, cursor = conectar()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inserir_gasto(descricao, valor, tipo):
    conn, cursor = conectar()
    cursor.execute('INSERT INTO gastos (descricao, valor, tipo) VALUES (?, ?, ?)',
                   (descricao, valor, tipo))
    conn.commit()
    conn.close()

def buscar_gastos():
    conn, cursor = conectar()
    cursor.execute('SELECT id, descricao, valor, tipo FROM gastos')
    resultados = cursor.fetchall()
    conn.close()
    return resultados