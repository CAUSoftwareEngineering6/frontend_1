import sys
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QDesktopWidget, QWidget, QListWidgetItem, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5 import uic
from Origin import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/main_window.ui", self)

        #########################################
        # 메뉴바 예시 -> 사용할 용도가 따로 있으면 사용하는 것도 좋을듯!
        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)

        # file menu action
        self.new_action = QAction("New")
        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.close)

        # help menu action
        self.doc_action = QAction("Documentation")
        self.release_action = QAction("Release Notes")
        self.license_action = QAction("View License")

        # file menu
        file_menu = self.menubar.addMenu("파일")
        file_menu.addAction(self.new_action)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_action)

        # help menu
        help_menu = self.menubar.addMenu("도움말")
        help_menu.addAction(self.doc_action)
        help_menu.addAction(self.release_action)
        help_menu.addAction(self.license_action)
        #########################################



        self.setFixedSize(800, 600)
        self.center()
        self.statusBar().showMessage('Main Page')

        self.origin = Origin(self)
        self.setCentralWidget(self.origin)
        self.origin.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def go_back_to_origin(self):
        self.origin = Origin(self)
        self.setCentralWidget(self.origin)
        self.statusBar().showMessage('Main Page')

    def go_back_to_user_list(self):
        self.user_list_page = UserListPage(self)
        self.setCentralWidget(self.user_list_page)
        self.statusBar().showMessage('User List Page')

    def go_back_to_group_list(self):
        self.group_list_page = GroupListPage(self)
        self.setCentralWidget(self.group_list_page)
        self.statusBar().showMessage('Group List Page')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
