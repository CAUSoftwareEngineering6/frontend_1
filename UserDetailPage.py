from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QListWidgetItem, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5 import uic

class UserDetailPage(QWidget):
    def __init__(self, main_window, detail):
        super().__init__()
        uic.loadUi("uis/detail_page.ui", self)

        self.main_window = main_window
        self.detailLabel.setText(detail)
        self.backButton.clicked.connect(self.go_back)

        layout = self.layout()
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def go_back(self):
        self.main_window.go_back_to_user_list()