from .User import User
from .Debate import Debate
from .Group import Group
from .Announcement import Announcement
from .Comment import Comment
from .StudentAndProfessor import *
import datetime


class MockDatabase:
    def __init__(self):
        self.users = self._create_mock_users()
        self.groups = self._create_mock_groups()

    def _create_mock_users(self):
        score = Score("출석", "중간", "기말", "과제", "등수")
        
        user1 = Student("1", "Alice", "pass", "alice@example.com", "female", "20192115", "성적1", score)
        user2 = Student("2", "user2", "password2", "user2@example.com", "female","학번2", "성적3", score)
        user3 = Student("3", "user3", "password3", "user3@example.com", "male", "학번3", "성적3", score)
        return [user1, user2, user3]

    def _create_mock_groups(self):
        # Creating mock users
        user1 = self.users[0]
        user2 = self.users[1]
        user3 = self.users[2]

        # Creating mock debates
        debate1 = Debate(user1, "역사란 무엇인가")
        debate2 = Debate(user2, "정의란 무엇인가")

        # Creating mock announcements
        announcement1 = Announcement(user1, "1차 공지입니다", "1차 공지 내용입니다")
        announcement2 = Announcement(user2, "2차 공지입니다", "2차 공지 내용입니다")

        #comment1 = Comment(user1, "토론 댓글")
        #comment2 = Comment(user2, "공지 댓글")
        #debate1.comments.append(comment1)
        #announcement1.comments.append(comment2)

        # Creating mock groups
        group1 = Group("1", "Group1")
        group1.add_member(user1)
        group1.add_member(user2)
        group1.add_debate(debate1)
        group1.add_debate(debate2)
        group1.add_announcement(announcement1)
        group1.add_announcement(announcement2)


        group2 = Group("2", "Group2")
        group2.add_member(user3)
        group2.add_debate(debate2)
        group2.add_announcement(announcement2)

        group3 = Group("3", "Group3")
        group3.add_member(user2)
        group3.add_member(user3)

        return [group1, group2, group3]

    def search_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return False

    def search_group(self, group_id):
        for group in self.groups:
            if group.group_id == group_id:
                return group
        return False

