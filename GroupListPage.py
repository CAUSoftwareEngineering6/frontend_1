from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QListWidgetItem, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5 import uic
from GroupDetailPage import GroupDetailPage

class GroupListPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("uis/group_list_page.ui", self)

        self.main_window = main_window
        self.backButton.clicked.connect(self.go_back)
        
        # 샘플 데이터 -> 실제 구현시 Group객체에서 받아올듯
        self.groups = ["Group 1", "Group 2", "Group 3"]
        for group in self.groups:
            item = QListWidgetItem(group)
            self.groupListWidget.addItem(item)
        
        self.groupListWidget.itemClicked.connect(self.open_detail_page)

        # 여백 주기
        layout = self.layout()
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def go_back(self):
        self.main_window.go_back_to_origin()

    def open_detail_page(self, item):
        self.detail_page = GroupDetailPage(self.main_window, item.text())
        self.main_window.setCentralWidget(self.detail_page)
        self.main_window.statusBar().showMessage('Group Detail Page')