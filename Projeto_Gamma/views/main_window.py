# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(760, 584)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 161, 41))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(180, 10, 201, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 10, 91, 31))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(540, 10, 151, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 50, 61, 41))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 60, 201, 21))
        self.comboBox.setEditable(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 140, 121, 31))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(210, 190, 401, 231))
        self.tableWidget.setColumnCount(4)
        self.BotaoExcluir = QPushButton(self.centralwidget)
        self.BotaoExcluir.setObjectName(u"BotaoExcluir")
        self.BotaoExcluir.setGeometry(QRect(500, 140, 111, 31))
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(540, 60, 141, 24))
        self.dateEdit.setCalendarPopup(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 60, 91, 31))
        self.label_Saldo = QLabel(self.centralwidget)
        self.label_Saldo.setObjectName(u"label_Saldo")
        self.label_Saldo.setGeometry(QRect(280, 440, 261, 31))
        self.BotaoEditarCategoria = QPushButton(self.centralwidget)
        self.BotaoEditarCategoria.setObjectName(u"BotaoEditarCategoria")
        self.BotaoEditarCategoria.setGeometry(QRect(360, 140, 111, 31))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 760, 33))
        self.menuFinancia_A = QMenu(self.menubar)
        self.menuFinancia_A.setObjectName(u"menuFinancia_A")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFinancia_A.menuAction())

        self.retranslateUi(mainWindow)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Descri\u00e7\u00e3o do tipo:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Valor:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Tipo:</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"Receita", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"Despesa", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("mainWindow", u"Receita", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"Adicionar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"Valor", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"Tipo", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWindow", u"data", None));
        self.BotaoExcluir.setText(QCoreApplication.translate("mainWindow", u"Excluir", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Data:</span></p></body></html>", None))
        self.label_Saldo.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.BotaoEditarCategoria.setText(QCoreApplication.translate("mainWindow", u"Editar ", None))
        self.menuFinancia_A.setTitle(QCoreApplication.translate("mainWindow", u"Financia A\u00ea", None))
    # retranslateUi

