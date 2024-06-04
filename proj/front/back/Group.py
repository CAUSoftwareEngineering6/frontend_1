from .User import *
from .Debate import *
from .Announcement import *
from .Post import *
import datetime
from typing import List

class Group:
    def __init__(self, group_id: str, group_name: str):
        self.group_id = group_id
        self.group_name = group_name
        self.members: List[User] = []
        self.debates: List[Debate] = []
        self.announcements: List[Announcement] = []


    def create_post(self, post_type):
        if post_type == "Announcement":
            # 추후 create_post 방식에 따라 구별
            announcement = Announcement()
            announcement.create_post()
        elif post_type == "Debate":
            debate = Debate()
            debate.create_post()

    def delete_post(self, post: Post):
        if isinstance(post, Announcement):
            self.announcements.remove(post)
        elif isinstance(post, Debate):
            self.debates.remove(post)
        # 만약 가비지 컬렉터가 작동하지 않는다면 추가 코드가 필요할듯

    def update_post(self, post: Post, name: str = None, content: str = None):
        if isinstance(post, Announcement):
            post.update_content(name, content)
        elif isinstance(post, Debate):
            post.update_content(name)

    def add_debate(self, debate: Debate):
        self.debates.append(debate)

    def add_announcement(self, announcement: Announcement):
        self.announcements.append(announcement)

    def add_member(self, user: User):
        self.members.append(user)

    def delete_member(self, user: User):
        self.members.remove(user)

    ## 수정부
    def check_user_access(self, user_id):
        for member in self.members:
            if user_id == member.student_id:
                return True
        return False

    def search_menber(self, user_id):
        for member in self.members:
                if user_id == member.user_id:
                    return member
        return False

    def search_debate(self, post_id):
        for post in self.debates:
                if post_id == post.post_id:
                    return post
        return False

    def search_announcement(self, post_id):
        for post in self.announcements:
            if post_id == post.post_id:
                return post
        return False