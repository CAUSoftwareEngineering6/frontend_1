from PyQt5.QtWidgets import QLineEdit, QApplication, QDesktopWidget, QWidget, QListWidget, QListWidgetItem, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtCore import Qt
from UserDetailPage import UserDetailPage


class UserListPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("사용자 검색")
        self.search_box.textChanged.connect(self.filter_users)
        layout.addWidget(self.search_box)

        self.userListWidget = QListWidget(self)
        layout.addWidget(self.userListWidget)

        self.users = [
            'Alice', 'Bob', 'Charlie', 'David'
        ]

        self.user_items = []
        for user in self.users:
            item = QListWidgetItem(user)
            self.userListWidget.addItem(item)
            self.user_items.append(item)

        self.userListWidget.itemClicked.connect(self.open_detail_page)

        self.backButton = QPushButton("로그인 페이지로 돌아가기", self)
        self.backButton.clicked.connect(self.go_back)
        layout.addWidget(self.backButton)

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(layout)

    def filter_users(self):
        search_text = self.search_box.text().lower()
        for item in self.user_items:
            item.setHidden(search_text not in item.text().lower())

    def open_detail_page(self, item):
        self.detail_page = UserDetailPage(self.main_window, item.text())
        self.main_window.setCentralWidget(self.detail_page)
        self.main_window.statusBar().showMessage('User Detail Page')

    def go_back(self):
        self.main_window.go_back_to_origin()

