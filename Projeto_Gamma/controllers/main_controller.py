# controllers/main_controller.py
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QInputDialog, QMessageBox, QVBoxLayout, QLabel, QLineEdit, QDialog, QDateEdit, QPushButton, QComboBox
from views.main_window import Ui_mainWindow
from database.dados import inserir_gasto, buscar_gastos, excluir_gasto, calcular_saldo_total, atualizar_lancamento
from PySide6.QtCore import QDate

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.carregar_lancamentos()
        self.ui.BotaoExcluir.clicked.connect(self.excluir_lancamento)
        self.atualizar_saldo()
        self.ui.BotaoEditarCategoria.clicked.connect(self.editar_lancamento)

        # conectar o botão ao método de adicionar o lançamemento
        self.ui.pushButton.clicked.connect(self.adicionar_lancamento)

    def atualizar_saldo(self):
        saldo = calcular_saldo_total()
        self.ui.label_Saldo.setText(f"Saldo atual: R$ {saldo:.2f}")

        if saldo >= 0:
            self.ui.label_Saldo.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.ui.label_Saldo.setStyleSheet("color: red; font-weight: bold;")

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

        self.atualizar_saldo()

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
        self.ui.dateEdit.setDate(QDate.currentDate())

        self.atualizar_saldo()

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

        self.atualizar_saldo()

    def editar_lancamento(self):
        linha = self.ui.tableWidget.currentRow()
        if linha == -1:
            print("Nenhuma linha selecionada.")
            return

        # pega os dados atuais da linha
        descricao = self.ui.tableWidget.item(linha, 0).text()
        valor = float(self.ui.tableWidget.item(linha, 1).text())
        tipo = self.ui.tableWidget.item(linha, 2).text()
        data = self.ui.tableWidget.item(linha, 3).text()

        dialog = EditarLancamentoDialog(descricao, valor, tipo, data, self)
        if dialog.exec() == QDialog.Accepted:
            nova_descricao, novo_valor, novo_tipo, nova_data = dialog.getDados()

            # atualiza no banco
            atualizar_lancamento(
                descricao, valor, tipo, data,
                nova_descricao, novo_valor, novo_tipo, nova_data
            )

            # atualiza na tabela
            self.ui.tableWidget.setItem(linha, 0, QTableWidgetItem(nova_descricao))
            self.ui.tableWidget.setItem(linha, 1, QTableWidgetItem(f"{novo_valor:.2f}"))
            self.ui.tableWidget.setItem(linha, 2, QTableWidgetItem(novo_tipo))
            self.ui.tableWidget.setItem(linha, 3, QTableWidgetItem(nova_data))

            self.atualizar_saldo()


class EditarLancamentoDialog(QDialog):
    def __init__(self, descricao, valor, tipo, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Lançamento")

        layout = QVBoxLayout()

        self.input_descricao = QLineEdit(descricao)
        self.input_valor = QLineEdit(str(valor))
        self.input_tipo = QComboBox()
        self.input_tipo.addItems(["Despesa", "Receita"])
        self.input_tipo.setCurrentText(tipo)
        self.input_data = QDateEdit()
        self.input_data.setDisplayFormat("yyyy-MM-dd")
        self.input_data.setDate(QDate.fromString(data, "yyyy-MM-dd"))

        layout.addWidget(QLabel("Descrição:"))
        layout.addWidget(self.input_descricao)

        layout.addWidget(QLabel("Valor:"))
        layout.addWidget(self.input_valor)

        layout.addWidget(QLabel("Tipo:"))
        layout.addWidget(self.input_tipo)

        layout.addWidget(QLabel("Data:"))
        layout.addWidget(self.input_data)

        botao_salvar = QPushButton("Salvar")
        botao_salvar.clicked.connect(self.accept)
        layout.addWidget(botao_salvar)

        self.setLayout(layout)

    def getDados(self):
        return (self.input_descricao.text(),
                float(self.input_valor.text()),
                self.input_tipo.currentText(),
                self.input_data.date().toString("yyyy-MM-dd"))