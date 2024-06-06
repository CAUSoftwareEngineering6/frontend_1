from PyQt5.QtWidgets import QInputDialog, QHBoxLayout, QListWidgetItem, QMessageBox, QLineEdit, QListWidget, QScrollArea, QTextEdit, QApplication, QDesktopWidget, QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy, QFrame
from PyQt5.QtCore import Qt


class NoticeDetailPage(QWidget):

    def __init__(self, main_window, group_id, post_id, group):
        super().__init__()
        self.post_id = post_id
        self.group = group
        self.group_id = group_id
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.announcement = self.main_window.get_all_announcement()
        for i in range(len(self.announcement)):
            if self.announcement[i]['post_id'] == self.post_id:
                self.announcement_post_name = self.announcement[i]['post_name']
                self.announcement_post_text = self.announcement[i]['content']

        # 전체 레이아웃
        main_layout = QVBoxLayout()

        # 제목과 내용 프레임
        content_frame = QFrame()
        content_layout = QVBoxLayout()

        # 공지 제목
        self.post_name = QLabel(f"{self.announcement_post_name}")
        self.post_name.setStyleSheet("font-weight: bold; font-size: 16px;")
        content_layout.addWidget(self.post_name)

        # 공지 내용
        self.post_text = QLabel(f"{self.announcement_post_text}")
        self.post_text.setWordWrap(True)
        self.post_text.setStyleSheet("font-size: 14px; margin-top: 10px;")
        content_layout.addWidget(self.post_text)

        content_frame.setLayout(content_layout)
        content_frame.setFrameShape(QFrame.StyledPanel)
        content_frame.setFrameShadow(QFrame.Raised)
        main_layout.addWidget(content_frame)

        # Spacer
        main_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 뒤로가기 버튼
        button_layout = QHBoxLayout()
        self.backButton = QPushButton("Back", self)
        self.backButton.setStyleSheet("padding: 10px 20px; font-size: 14px;")
        self.backButton.clicked.connect(self.go_back)
        button_layout.addWidget(self.backButton, alignment=Qt.AlignRight)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.setStyleSheet("padding: 20px;")

    def go_back(self):
        self.main_window.go_back_to_notice_page(self.group)