# controllers/main_controller.py
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from views.main_window import Ui_mainWindow
from database.dados import inserir_gasto, buscar_gastos, excluir_gasto

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.carregar_lancamentos()
        self.ui.BotaoExcluir.clicked.connect(self.excluir_lancamento)

        # conectar o botão ao método de adicionar o lançamemento
        self.ui.pushButton.clicked.connect(self.adicionar_lancamento)

    def carregar_lancamentos(self):
        self.ui.tableWidget.setRowCount(0) # limpa a tabela antes de carregar

        registros = buscar_gastos() # busca os dados no banco de dados

        for registro in registros:
            _, descricao, valor, tipo, data = registro
            linha = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(linha)
            self.ui.tableWidget.setItem(linha, 0, QTableWidgetItem(descricao))
            self.ui.tableWidget.setItem(linha, 1, QTableWidgetItem(f'{valor:.2f}'))
            self.ui.tableWidget.setItem(linha, 2, QTableWidgetItem(tipo))
            self.ui.tableWidget.setItem(linha, 3, QTableWidgetItem(data))

    def adicionar_lancamento(self):
        # Pegando os valores dos campos
        descricao = self.ui.lineEdit.text()
        valor_texto = self.ui.lineEdit_2.text()
        tipo = self.ui.comboBox.currentText()
        data_qdate = self.ui.dateEdit.date()  # pega a data do QDateEdit
        data = data_qdate.toString("yyyy-MM-dd")  # converte para string no formato padrão

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
        inserir_gasto(descricao, valor, tipo, data)
        # Pegando o número atual de linhas da tabela
        linha = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(linha)  # adiciona uma nova linha

        # Inserindo os dados nas células
        self.ui.tableWidget.setItem(linha, 0, QTableWidgetItem(descricao))
        self.ui.tableWidget.setItem(linha, 1, QTableWidgetItem(f"{valor:.2f}"))
        self.ui.tableWidget.setItem(linha, 2, QTableWidgetItem(tipo))
        self.ui.tableWidget.setItem(linha, 3, QTableWidgetItem(data)) #coluna data


        # limpar os campos após adicionar:
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.comboBox.setCurrentIndex(0)

    def excluir_lancamento(self):
        linha_selecionada = self.ui.tableWidget.currentRow()
        if linha_selecionada == -1:
            print("Nenhuma linha selecionada.")
            return

        item_descricao = self.ui.tableWidget.item(linha_selecionada, 0)
        item_valor = self.ui.tableWidget.item(linha_selecionada, 1)
        item_tipo = self.ui.tableWidget.item(linha_selecionada, 2)
        item_data = self.ui.tableWidget.item(linha_selecionada, 3)

        if not item_descricao or not item_valor or not item_tipo or not item_data:
            print("Dados inválidos na linha selecionada.")
            return

        descricao = item_descricao.text()
        valor = float(item_valor.text())
        tipo = item_tipo.text()
        data = item_data.text()

        # Remove do banco
        excluir_gasto(descricao, valor, tipo, data)

        # Remove da tabela
        self.ui.tableWidget.removeRow(linha_selecionada)