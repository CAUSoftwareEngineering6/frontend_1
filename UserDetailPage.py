from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton

class UserDetailPage(QWidget):
    def __init__(self, main_window, detail):
        super().__init__()
        self.main_window = main_window
        self.detail = detail
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # QLabel for detail
        self.detailLabel = QLabel(self.detail, self)
        layout.addWidget(self.detailLabel)

        # QPushButton for back
        self.backButton = QPushButton("Back", self)
        self.backButton.clicked.connect(self.go_back)
        layout.addWidget(self.backButton)

        # Adding a spacer item to the layout
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

    def go_back(self):
        self.main_window.go_back_to_user_list()
