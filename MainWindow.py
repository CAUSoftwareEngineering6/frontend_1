import sys
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QDesktopWidget, QWidget, QListWidgetItem, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5 import uic
from Origin import *
from LoginWindow import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/main_window.ui", self)

        #########################################
        # 메뉴바 예시 -> 사용할 용도가 따로 있으면 사용하는 것도 좋을 것 같습니다.
        # 우선 종료 및 사용자 정보만 간략하게 표시하는 용도로 넣어뒀습니다.
        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)

        # file menu action
        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.close)

        # help menu action
        self.doc_action = QAction("이름")
        self.release_action = QAction("학번")

        # file menu
        file_menu = self.menubar.addMenu("종료")
        file_menu.addAction(self.quit_action)

        # help menu
        help_menu = self.menubar.addMenu("내 정보")
        help_menu.addAction(self.doc_action)
        help_menu.addAction(self.release_action)
        ########################################

        ## 최초의 로그인 페이지 열기
        self.login = LoginWindow(self)
        self.setGeometry(100, 100, 300, 150)
        self.center()
        self.setCentralWidget(self.login)
        self.login.show()
        self.username = 'Alice'

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#----------------뒤로 가기 버튼 관련 함수-------------------#
    def go_back_to_login(self):
        self.login = LoginWindow(self)
        self.setGeometry(100, 100, 300, 150)
        self.center()
        self.setCentralWidget(self.login)
        self.statusBar().showMessage('Login Page')

    def go_back_to_origin(self):
        self.origin = Origin(self)
        self.setGeometry(100, 100, 400, 500)
        self.center()
        self.setCentralWidget(self.origin)
        self.statusBar().showMessage('Main Page')

    def go_back_to_user_list(self):
        self.user_list_page = UserListPage(self)
        self.setGeometry(100, 100, 400, 500)
        self.center()
        self.setCentralWidget(self.user_list_page)
        self.statusBar().showMessage('User List Page')

    def go_back_to_group_list(self):
        self.group_list_page = GroupListWindow(self, self.username)
        self.setGeometry(100, 100, 400, 500)
        self.center()
        self.setCentralWidget(self.group_list_page)
        self.statusBar().showMessage('Group List Page')
    
    def go_back_to_select_page(self, group):
        self.group_select_page = GroupSelectWindow(group, self)
        self.setGeometry(100, 100, 400, 500)
        self.center()
        self.setCentralWidget(self.group_select_page)
        self.statusBar().showMessage(group['name'] + ' Select Page')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
