from PyQt5.QtWidgets import QLineEdit, QTextEdit, QApplication, QDesktopWidget, QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QPushButton, QListWidget, QListWidgetItem


class UserCreatePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle('뒤로 가기')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.go_back_button = QPushButton('뒤로가기')
        self.go_back_button.clicked.connect(self.go_back)
        layout.addWidget(self.go_back_button)

        self.userid_label = QLabel('User id')
        layout.addWidget(self.userid_label)
        self.userid_input = QLineEdit()
        layout.addWidget(self.userid_input)

        self.username_label = QLabel('User name')
        layout.addWidget(self.username_label)
        self.username_input = QLineEdit()
        layout.addWidget(self.username_input)

        self.password_label = QLabel('Password')
        layout.addWidget(self.password_label)
        self.password_input = QLineEdit()
        layout.addWidget(self.password_input)

        self.email_label = QLabel('Eamil')
        layout.addWidget(self.email_label)
        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        self.gender_label = QLabel('Gender')
        layout.addWidget(self.gender_label)
        self.gender_input = QLineEdit()
        layout.addWidget(self.gender_input)

        self.create_button = QPushButton('Create')
        self.go_back_button.clicked.connect(self.create_user)
        layout.addWidget(self.create_button)

        self.setLayout(layout)
    def create_user(self):
        # 빈 필드에서 text추출하는 부분
        self.main_window.create_user()
        self.show()

    def go_back(self):
        self.main_window.go_back_to_user_list()

    def create_user(self):
        user_id = self.userid_label.text()
        username = self.username_label.text()
        password = self.password_label.text()
        email = self.email_label.text()
        gender = self.gender_label.text()
        self.main_window.create_user(user_id, username, password, email, gender)
        # 삭제 완료 문구 알림창 뜨고 -> 알림창 확인 클릭시 go_back()호출

