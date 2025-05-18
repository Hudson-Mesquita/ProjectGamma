# controllers/main_controller.py
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from views.main_window import Ui_mainWindow
from database.dados import inserir_gasto, buscar_gastos

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.carregar_lancamentos()

        # conectar o botão ao método de adicionar o lançamemento
        self.ui.pushButton.clicked.connect(self.adicionar_lancamento)

    def carregar_lancamentos(self):
        self.ui.tableWidget.setRowCount(0) # limpa a tabela antes de carregar

        registros = buscar_gastos() # busca os dados no banco de dados

        for registro in registros:
            _, descricao, valor, tipo = registro
            linha = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(linha)
            self.ui.tableWidget.setItem(linha, 0, QTableWidgetItem(descricao))
            self.ui.tableWidget.setItem(linha, 1, QTableWidgetItem(f'{valor:.2f}'))
            self.ui.tableWidget.setItem(linha, 2, QTableWidgetItem(tipo))

    def adicionar_lancamento(self):
        # Pegando os valores dos campos
        descricao = self.ui.lineEdit.text()
        valor_texto = self.ui.lineEdit_2.text()
        tipo = self.ui.comboBox.currentText()

        # Validando os dados
        if not descricao or not valor_texto:
            print("Descrição e valor são obrigatórios.")
            return

        try:
            valor = float(valor_texto)
        except ValueError:
            print("Valor inválido. Digite um número.")
            return


        # inserindo no banco de dados
        inserir_gasto(descricao, valor, tipo)
        # Pegando o número atual de linhas da tabela
        linha = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(linha)  # adiciona uma nova linha

        # Inserindo os dados nas células
        self.ui.tableWidget.setItem(linha, 0, QTableWidgetItem(descricao))
        self.ui.tableWidget.setItem(linha, 1, QTableWidgetItem(f"{valor:.2f}"))
        self.ui.tableWidget.setItem(linha, 2, QTableWidgetItem(tipo))


        # limpar os campos após adicionar:
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.comboBox.setCurrentIndex(0)