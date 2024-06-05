from PyQt5.QtWidgets import QInputDialog, QHBoxLayout, QListWidgetItem, QMessageBox, QLineEdit, QListWidget, QScrollArea, QTextEdit, QApplication, QDesktopWidget, QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy

class NoticePage(QWidget):
    saved_data = {}  # 그룹별 저장된 공지 및 토론 데이터

    def __init__(self, group, main_window, group_id, username):
        super().__init__()
        self.group = group
        self.group_id = group_id
        self.username = username
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        # 여기서 데이터를 읽어와서 하나씩 집어넣음
        self.announcement = self.main_window.get_all_announcement()

        self.layout = QVBoxLayout()

        # 뒤로가기 버튼
        self.back_button = QPushButton('뒤로가기')
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.notice_label = QLabel('공지란')
        self.layout.addWidget(self.notice_label)

        self.notice_input = QTextEdit()
        self.notice_input.setFixedHeight(100)  # 공지 작성 박스 높이 조정
        self.layout.addWidget(self.notice_input)

        self.notice_button = QPushButton('공지 작성')
        self.notice_button.clicked.connect(self.add_notice)
        self.layout.addWidget(self.notice_button)

        self.notice_list = QListWidget()
        self.layout.addWidget(self.notice_list)

        #ScrollArea로 감싸기
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_widget.setLayout(self.layout)
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)

        self.show()

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def go_back(self):
        print("back")
        self.main_window.go_back_to_select_page(self.group)

    def add_notice(self):
        notice_text = self.notice_input.toPlainText()
        if notice_text:
            self.add_notice_item(notice_text)
            self.notice_input.clear()
        else:
            QMessageBox.warning(self, 'Error', '공지 내용을 입력하세요.')

    def add_notice_item(self, text):
        self.main_window.manager.create_announcement("1", self.main_window.group_id, text, None)
        self.show()

    def show(self):
        # 기존의 공지 테이블 지우기
        self.notice_list.clear()

        # announcement 정보 가져오기
        announcement = self.main_window.get_all_announcement()

        for i in range(len(announcement)):
            item = QListWidgetItem()
            post_id = announcement[i]['post_id']
            widget = QWidget()
            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            post_id = announcement[i]['post_id']

            label = QLabel(f"{post_id}. {announcement[i]['post_name']}")
            label.setWordWrap(True)
            layout.setSpacing(10)
            layout.addWidget(label)

            edit_button = QPushButton(f'✎')
            edit_button.setFixedSize(30, 30)
            edit_button.clicked.connect(lambda _,post_id=post_id, label=label:self.edit_notice(post_id, label))
            layout.addWidget(edit_button)

            delete_button = QPushButton(f'✖')
            delete_button.setFixedSize(30, 30)
            delete_button.clicked.connect(lambda _,post_id=post_id: self.delete_notice(post_id))
            layout.addWidget(delete_button)

            widget.setLayout(layout)
            item.setSizeHint(widget.sizeHint())
            self.notice_list.addItem(item)
            self.notice_list.setItemWidget(item, widget)

    def delete_notice(self, post_id):
        self.main_window.manager.delete_announcement(self.main_window.group_id, post_id)
        self.show()

    def edit_notice(self, post_id, label):
        current_text = label.text().split(". ", 1)[1]
        text, ok = QInputDialog.getText(self, '공지 수정', '새로운 공지 내용을 입력하세요:', text=current_text)
        self.main_window.manager.update_announcement(self.main_window.group_id, post_id, text, None)
        if ok and text:
            self.show()
