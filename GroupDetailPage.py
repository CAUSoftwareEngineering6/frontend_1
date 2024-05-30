from PyQt5.QtWidgets import QInputDialog, QHBoxLayout, QListWidgetItem, QMessageBox, QLineEdit, QListWidget, QScrollArea, QTextEdit, QApplication, QDesktopWidget, QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy

class GroupDetailPage(QWidget):
    saved_data = {}  # 그룹별 저장된 공지 및 토론 데이터

    def __init__(self, group, main_window, view):
        super().__init__()
        self.group = group
        self.main_window = main_window
        self.view = view
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.group['name'])
        self.setGeometry(100, 100, 600, 700)

        self.layout = QVBoxLayout()

        # 뒤로가기 버튼
        self.back_button = QPushButton('뒤로가기')
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        if self.view == 'notice':
            self.init_notice_board()
        elif self.view == 'discussion':
            self.init_discussion_board()

        # ScrollArea로 감싸기
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_widget.setLayout(self.layout)
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

        # 저장된 데이터 로드
        if self.group['name'] in GroupDetailPage.saved_data:
            saved_notices, saved_discussions = GroupDetailPage.saved_data[self.group['name']]
            if self.view == 'notice':
                for notice in saved_notices:
                    self.add_notice_item(notice)
            elif self.view == 'discussion':
                for discussion, replies in saved_discussions:
                    self.add_discussion_item(discussion, replies)

    def init_notice_board(self):
        # 공지란
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

    def init_discussion_board(self):
        # 토론란
        self.discussion_label = QLabel('토론란')
        self.layout.addWidget(self.discussion_label)

        self.discussion_input = QLineEdit()
        self.discussion_input.setPlaceholderText('토론 주제 입력')
        self.layout.addWidget(self.discussion_input)

        self.discussion_button = QPushButton('토론 주제 작성')
        self.discussion_button.clicked.connect(self.add_discussion)
        self.layout.addWidget(self.discussion_button)

        self.discussion_list = QListWidget()
        self.layout.addWidget(self.discussion_list)

    def go_back(self):
        self.main_window.go_back_to_select_page(self.group)


    def add_notice(self):
        notice_text = self.notice_input.toPlainText()
        if notice_text:
            self.add_notice_item(notice_text)
            self.notice_input.clear()
        else:
            QMessageBox.warning(self, 'Error', '공지 내용을 입력하세요.')

    def add_notice_item(self, text):
        item = QListWidgetItem()

        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel(f"{self.notice_list.count() + 1}. {text}")
        label.setWordWrap(True)
        layout.setSpacing(10)
        layout.addWidget(label)

        edit_button = QPushButton('✎')
        edit_button.setFixedSize(30, 30)
        edit_button.clicked.connect(lambda _, i=item, l=label: self.edit_notice(i, l))
        layout.addWidget(edit_button)

        delete_button = QPushButton('✖')
        delete_button.setFixedSize(30, 30)
        delete_button.clicked.connect(lambda _, i=item: self.delete_notice(i))
        layout.addWidget(delete_button)

        widget.setLayout(layout)
        item.setSizeHint(widget.sizeHint())
        self.notice_list.addItem(item)
        self.notice_list.setItemWidget(item, widget)

    def edit_notice(self, item, label):
        current_text = label.text().split(". ", 1)[1]
        text, ok = QInputDialog.getText(self, '공지 수정', '새로운 공지 내용을 입력하세요:', text=current_text)
        if ok and text:
            label.setText(f"{self.notice_list.row(item) + 1}. {text}")

    def delete_notice(self, item):
        row = self.notice_list.row(item)
        self.notice_list.takeItem(row)
        for i in range(row, self.notice_list.count()):
            list_item = self.notice_list.item(i)
            label = self.notice_list.itemWidget(list_item).layout().itemAt(0).widget()
            label.setText(f"{i + 1}. {label.text().split('. ', 1)[1]}")

    def add_discussion(self):
        discussion_text = self.discussion_input.text()
        if discussion_text:
            self.add_discussion_item(discussion_text)
            self.discussion_input.clear()
        else:
            QMessageBox.warning(self, 'Error', '토론 주제를 입력하세요.')

    def add_discussion_item(self, text, replies=None):
        item = QListWidgetItem()

        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        topic_layout = QHBoxLayout()
        topic_label = QLabel(f"{self.discussion_list.count() + 1}. {text}")
        topic_label.setWordWrap(True)
        topic_layout.addWidget(topic_label)

        edit_button = QPushButton('✎')
        edit_button.setFixedSize(30, 30)
        edit_button.clicked.connect(lambda _, i=item, l=topic_label: self.edit_discussion(i, l))
        topic_layout.addWidget(edit_button)

        delete_button = QPushButton('✖')
        delete_button.setFixedSize(30, 30)
        delete_button.clicked.connect(lambda _, i=item: self.delete_discussion(i))
        topic_layout.addWidget(delete_button)

        layout.addLayout(topic_layout)

        reply_layout = QVBoxLayout()
        reply_scroll = QScrollArea()
        reply_scroll.setWidgetResizable(True)
        reply_widget = QWidget()
        reply_widget.setLayout(reply_layout)
        reply_scroll.setWidget(reply_widget)
        reply_scroll.setFixedHeight(150)  # 댓글 리스트 높이 설정

        if replies:
            for reply in replies:
                self.add_reply_item(reply, reply_layout)

        reply_input_layout = QHBoxLayout()
        reply_input = QLineEdit()
        reply_input_layout.addWidget(reply_input)
        reply_button = QPushButton('댓글 작성')
        reply_button.clicked.connect(lambda _, i=item, ri=reply_input, rl=reply_layout: self.add_reply(i, ri, rl))
        reply_input_layout.addWidget(reply_button)

        layout.addWidget(reply_scroll)
        layout.addLayout(reply_input_layout)

        widget.setLayout(layout)
        item.setSizeHint(widget.sizeHint())
        item.setData(1, replies or [])
        self.discussion_list.addItem(item)
        self.discussion_list.setItemWidget(item, widget)

    def edit_discussion(self, item, label):
        current_text = label.text().split(". ", 1)[1]
        text, ok = QInputDialog.getText(self, '토론 수정', '새로운 토론 주제를 입력하세요:', text=current_text)
        if ok and text:
            label.setText(f"{self.discussion_list.row(item) + 1}. {text}")

    def delete_discussion(self, item):
        row = self.discussion_list.row(item)
        self.discussion_list.takeItem(row)
        for i in range(row, self.discussion_list.count()):
            list_item = self.discussion_list.item(i)
            label = self.discussion_list.itemWidget(list_item).layout().itemAt(0).layout().itemAt(0).widget()
            label.setText(f"{i + 1}. {label.text().split('. ', 1)[1]}")

    def add_reply(self, item, reply_input, reply_layout):
        text = reply_input.text()
        if text:
            self.add_reply_item(text, reply_layout)
            item.data(1).append(text)
            reply_input.clear()
        else:
            QMessageBox.warning(self, 'Error', '댓글 내용을 입력하세요.')

    def add_reply_item(self, text, layout):
        label = QLabel(f" - {text}")
        label.setWordWrap(True)
        layout.addWidget(label)

    def get_list_item_text(self, item):
        label = self.notice_list.itemWidget(item).layout().itemAt(0).widget()
        return label.text().split('. ', 1)[1]
