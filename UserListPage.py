from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QListWidgetItem, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5 import uic
from UserDetailPage import *

class UserListPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("uis/user_list_page.ui", self)

        self.main_window = main_window
        self.backButton.clicked.connect(self.go_back)
        
        # 샘플 데이터
        self.users = ["User 1", "User 2", "User 3"]
        for user in self.users:
            item = QListWidgetItem(user)
            self.userListWidget.addItem(item)
        
        self.userListWidget.itemClicked.connect(self.open_detail_page)

        # 여백 주기
        layout = self.layout()
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def go_back(self):
        self.main_window.go_back_to_origin()

    def open_detail_page(self, item):
        self.detail_page = UserDetailPage(self.main_window, item.text())
        self.main_window.setCentralWidget(self.detail_page)
        self.main_window.statusBar().showMessage('User Detail Page')