from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QListWidget, QListWidgetItem, QVBoxLayout, \
    QSpacerItem, QSizePolicy, QPushButton
from GroupDetailPage import GroupDetailPage
from LoginWindow import *
from GroupSelectPage import *


class GroupListPage(QWidget):
    def __init__(self, main_window, username, group_id):
        super().__init__()
        self.username = username
        self.group_id = group_id
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Group List')
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("그룹 또는 사용자 검색")
        self.search_box.textChanged.connect(self.filter_groups)
        self.layout.addWidget(self.search_box)

        # 여기서 데이터 다 읽어오고, 나머지는 기존 코드 활용
        self.groups = self.main_window.get_all_group()

        self.group_boxes = []
        for group in self.groups:
            group_box = self.create_group_box(group)
            self.group_boxes.append(group_box)
            self.layout.addWidget(group_box)

        # 뒤로가기 버튼
        self.back_button = QPushButton('선택 페이지로 돌아가기')
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def create_group_box(self, group):
        group_box = QGroupBox(group['group_name'])
        group_layout = QVBoxLayout()

        info_layout = QHBoxLayout()
        label = QLabel(f"학생 {group['member_num']} 명")
        info_layout.addWidget(label)

        # group_name -> member_name
        if group['accessible'] == True:
            visit_button = QPushButton('방문')
            visit_button.clicked.connect(lambda _, g=group: self.visit_group(g))
            info_layout.addWidget(visit_button)
        else:
            lock_button = QPushButton()
            lock_button.setText('🔒')
            lock_button.clicked.connect(lambda _, g=group, gb=group_box: self.toggle_members(g, gb))
            info_layout.addWidget(lock_button)

        group_layout.addLayout(info_layout)
        # group_name -> member_name
        members_label = QLabel("\n".join(group['group_name']))
        members_label.setVisible(False)
        group_layout.addWidget(members_label)

        group_box.setLayout(group_layout)
        group_box.members_label = members_label
        return group_box

    def toggle_members(self, group, group_box):
        members_label = group_box.members_label
        members_label.setVisible(members_label.isVisible() == 0)

    def filter_groups(self):
        search_text = self.search_box.text().lower()
        for i, group in enumerate(self.groups):
            group_box = self.group_boxes[i]
            if search_text in group['group_name'].lower():
                group_box.show()
            else:
                group_box.hide()

    def visit_group(self, group):
        self.group_select_window = GroupSelectPage(group, self.main_window, self.group_id, self.username)
        self.main_window.setCentralWidget(self.group_select_window)
        self.main_window.statusBar().showMessage(group['group_name'] + ' Select Page')

    def go_back(self):
        self.main_window.go_back_to_origin()
