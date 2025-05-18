# controllers/main_controller.py
from PySide6.QtWidgets import QMainWindow
from views.main_window import Ui_MainWindow

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)