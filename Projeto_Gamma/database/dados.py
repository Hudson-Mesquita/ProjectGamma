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
            tipo TEXT NOT NULL,
            data TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inserir_gasto(descricao, valor, tipo, data):
    conn, cursor = conectar()
    cursor.execute('INSERT INTO gastos (descricao, valor, tipo, data) VALUES (?, ?, ?, ?)',
                   (descricao, valor, tipo, data))
    conn.commit()
    conn.close()

def buscar_gastos():
    conn, cursor = conectar()
    cursor.execute('SELECT id, descricao, valor, tipo, data FROM gastos')
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def excluir_gasto(descricao, valor, tipo, data):
    conn, cursor = conectar()
    cursor.execute('''
        DELETE FROM gastos
        WHERE id = (
            SELECT id FROM gastos
            WHERE descricao = ? AND valor = ? AND tipo = ? AND data = ?
            LIMIT 1
        )
    ''', (descricao, valor, tipo, data))
    conn.commit()
    conn.close()

def calcular_saldo_total():
    conn, cursor = conectar()
    cursor.execute("SELECT valor, tipo FROM gastos")
    registros = cursor.fetchall()
    conn.close()

    saldo = 0.0
    for valor, tipo in registros:
        if tipo.lower() == 'receita':
            saldo += valor
        elif tipo.lower() == 'despesa':
            saldo -= valor
    return saldo
