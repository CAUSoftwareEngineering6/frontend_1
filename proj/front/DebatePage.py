from PyQt5.QtWidgets import QInputDialog, QHBoxLayout, QListWidgetItem, QMessageBox, QLineEdit, QListWidget, QScrollArea, QTextEdit, QApplication, QDesktopWidget, QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy

class DebatePage(QWidget):

    def __init__(self, group, main_window, group_id, username):
        super().__init__()
        self.group = group
        self.group_id = group_id
        self.username = username
        self.main_window = main_window
        self.initUI()

    def initUI(self):

        self.layout = QVBoxLayout()
        # 뒤로가기 버튼
        self.back_button = QPushButton('뒤로가기')
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

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


        # ScrollArea로 감싸기
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
        self.main_window.go_back_to_select_page(self.group)

    def add_discussion(self):
        discussion_text = self.discussion_input.text()
        if discussion_text:
            self.add_discussion_item(discussion_text)
            self.discussion_input.clear()
        else:
            QMessageBox.warning(self, 'Error', '토론 주제를 입력하세요.')

    def add_discussion_item(self, text):
        print("asdf")
        self.main_window.manager.create_debate("1", self.main_window.group_id, text)
        self.show()


    def show(self):
        # 기존의 토론 테이블 지우기
        self.discussion_list.clear()

        # debate 정보 가져오기
        debate = self.main_window.get_all_debate()


        for i in range(0,len(debate)):
            print("isi == ", i)
            replies = None
            item = QListWidgetItem()
            widget = QWidget()
            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(10)
            post_id = debate[i]['post_id']

            topic_layout = QHBoxLayout()
            topic_label = QLabel(f"{post_id}. {debate[i]['post_name']}")
            topic_label.setWordWrap(True)
            topic_layout.addWidget(topic_label)

            edit_button = QPushButton('✎')
            edit_button.setFixedSize(30, 30)
            edit_button.clicked.connect(lambda _, post_id = post_id, label = topic_label : self.edit_discussion(post_id, label))
            topic_layout.addWidget(edit_button)

            delete_button = QPushButton('✖')
            delete_button.setFixedSize(30, 30)
            delete_button.clicked.connect(lambda _, post_id = post_id: self.delete_discussion(post_id))
            topic_layout.addWidget(delete_button)

            layout.addLayout(topic_layout)

            reply_layout = QVBoxLayout()
            reply_scroll = QScrollArea()
            reply_scroll.setWidgetResizable(True)
            reply_widget = QWidget()
            reply_widget.setLayout(reply_layout)
            reply_scroll.setWidget(reply_widget)
            reply_scroll.setFixedHeight(150)  # 댓글 리스트 높이 설정

            reply_input_layout = QHBoxLayout()
            reply_input = QLineEdit()
            reply_input_layout.addWidget(reply_input)
            reply_button = QPushButton('댓글 작성')

            comment_list = QListWidget()
            reply_button.clicked.connect(lambda _, item = item, reply_input = reply_input, post_id = post_id, i = i, reply_layout = reply_layout, comment_list = comment_list: self.add_reply(item, reply_input, post_id, i, reply_layout, comment_list))



            reply_input_layout.addWidget(reply_button)
            self.reply_label = QLabel()

            self.show_reply(i, reply_layout, comment_list)
            reply_layout.addWidget(comment_list)


            layout.addWidget(reply_scroll)
            layout.addLayout(reply_input_layout)

            widget.setLayout(layout)
            item.setSizeHint(widget.sizeHint())
            item.setData(1, replies or [])
            self.discussion_list.addItem(item)
            self.discussion_list.setItemWidget(item, widget)



    def edit_discussion(self, post_id, label):
        current_text = label.text().split(". ", 1)[1]
        text, ok = QInputDialog.getText(self, '토론 수정', '새로운 토론 주제를 입력하세요:', text=current_text)
        self.main_window.manager.update_debate(self.main_window.group_id, post_id, text)
        if ok and text:
            self.show()

    def delete_discussion(self, post_id):
        self.main_window.manager.delete_debate(self.main_window.group_id, post_id)
        self.show()


    def add_reply(self, item, reply_input, post_id, index, layout, comment_list):
        text = reply_input.text()
        print("iddex_id =", index,"post_id =", post_id)
        if text:
            self.add_reply_item(post_id, text, index, layout, comment_list)
            item.data(1).append(text)
            reply_input.clear()
        else:
            QMessageBox.warning(self, 'Error', '댓글 내용을 입력하세요.')

    def show_reply(self, index, layout, comment_list):

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        comment_list.clear()
        debate = self.main_window.get_all_debate()
        post_id = debate[index]['post_id']

        for i in range(len(debate)):
            if i == index :

                for j in range(len(debate[i]['comment_list'])):
                    item = QListWidgetItem()
                    comment_id = debate[i]['comment_list'][j]['comment_id']
                    widget = QWidget()
                    comment_layout = QHBoxLayout()
                    comment_layout.setContentsMargins(0, 0, 0, 0)

                    reply_label = QLabel(f" - {debate[i]['comment_list'][j]['comment_content']}")
                    reply_label.setWordWrap(True)
                    comment_layout.setSpacing(10)
                    comment_layout.addWidget(reply_label)

                    layout.addWidget(reply_label)

                    edit_button = QPushButton('✎')
                    edit_button.setFixedSize(30, 30)
                    edit_button.clicked.connect(lambda _, post_id = post_id, reply_label = reply_label, comment_id = comment_id, index = index, layout = layout, comment_list = comment_list:self.edit_comment(post_id, reply_label, comment_id, index, layout, comment_list))
                    comment_layout.addWidget(edit_button)

                    delete_button = QPushButton('✖')
                    delete_button.setFixedSize(30, 30)
                    delete_button.clicked.connect(lambda _, post_id = post_id, index = index, layout = layout, comment_list = comment_list, d = debate[i]['comment_list'][j]['comment_id']: self.delete_comment(post_id, index, layout, comment_list, d))
                    comment_layout.addWidget(delete_button)

                    widget.setLayout(comment_layout)
                    item.setSizeHint(widget.sizeHint())
                    comment_list.addItem(item)
                    comment_list.setItemWidget(item, widget)







    def add_reply_item(self, post_id, text, index, layout, comment_list):
        self.main_window.manager.create_debate_comment("1", self.main_window.group_id, post_id, text)
        self.show_reply(index, layout, comment_list)

    def get_list_item_text(self, item):
        label = self.notice_list.itemWidget(item).layout().itemAt(0).widget()
        return label.text().split('. ', 1)[1]

    def delete_comment(self, post_id, index, layout, comment_list, comment_id):
        self.main_window.manager.delete_debate_comment(self.main_window.group_id, post_id, comment_id)
        self.show_reply(index, layout, comment_list)

    def edit_comment(self, post_id, label, comment_id, index, layout, comment_list):
        current_text = label.text().split(' ', 1)[1]
        text, ok = QInputDialog.getText(self, '답글 수정', '새로운 답급을 입력하세요:', text=current_text)
        self.main_window.manager.update_debate_comment(self.main_window.group_id, post_id, comment_id, text)
        if ok and text:
            self.show_reply(index, layout, comment_list)
