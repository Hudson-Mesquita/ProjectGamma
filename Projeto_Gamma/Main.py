import sys
from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainController
from database.dados import criar_tabela

if __name__ == "__main__":
    criar_tabela() # cria a tabela se não existir

    app = QApplication(sys.argv)
    window = MainController()
    window.show()
    sys.exit(app.exec())