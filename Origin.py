from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QListWidgetItem, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5 import uic
from GroupListPage import *
from UserListPage import *
from LoginWindow import *

class Origin(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("uis/origin.ui", self)

        self.main_window = main_window
        self.userListButton.clicked.connect(self.open_user_list_page)
        self.groupListButton.clicked.connect(self.open_group_list_page)

        # 여백 주기
        layout = self.layout()
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def open_user_list_page(self):
        self.user_list_page = UserListPage(self.main_window)
        self.main_window.setCentralWidget(self.user_list_page)
        self.main_window.statusBar().showMessage('User List Page')

    def open_group_list_page(self):
        self.group_list_page = GroupListWindow(self.main_window, username=self.main_window.username)
        self.main_window.setCentralWidget(self.group_list_page)
        self.main_window.statusBar().showMessage('Group List Page')