from .User import *
from .Score import *
from .Post import *
from typing import List
from .Management import *

class Student(User):
    def __init__(self,user_id: str, username: str, password: str, email: str, gender: str, student_id: int, grade: str, score: Score):
        super().__init__(user_id, username, password, email, gender)
        self.student_id = student_id
        self.grade = grade
        self.score = score

    def get_grade(self):
        return {
		"attendance": self.score.attendance,
		"midterm" : self.score.midterm,
		"final" : self.score.final,
		"assignment" : self.score.assignment,
		"Whole score" : self.score.cal_score()		
	}

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            "student_id": self.student_id,
            "grade": self.grade
        })
        return base_dict

    def get_detail(self, current_user_id):
        detail = self.to_dict()
        if current_user_id == self.user_id:
            detail["score"] = {
                "attendance": self.score.attendance,
                "midterm": self.score.midterm,
                "final": self.score.final,
                "assignment": self.score.assignment,
                "whole_score": self.score.cal_score()
            }
        return detail

class Professor(User):
    def __init__(self, user_id: str, username: str, password: str, email: str, gender: str, professor_id: int, rand: str):
        super().__init__(user_id, username, password, email, gender)
        self.professor_id = professor_id
        self.rand = rand

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            "professor_id": self.professor_id,
            "rand": self.rand
        })
        return base_dict

    # 이 부분도 정확히 이해가 안되서 우선 제 방식대로 바꾸고 나중에 만나서 이야기해보면 좋을거같아요!
    # def create_user(self, user: User, management: management):
    #     return management.create_user(user)
    #
    # def delete_user(self, user_id: str, management: management):
	#      return management.delete_user(user_id)
    #
    # def create_group(self, group_id: int, group_name: str, management:management):
    #     return management.create_group(group_id, group_name)
	#
    # def delete_group(self, group_id: int, management):
    #     return management.delete_group(group_id)
    #
    # def update_group_name(self, group_id : int, new_group_name: str, management: management):
	# group = management.getgroup()
	# for findgroup in group:
	# 	if group_id == findgroup.id:
	# 		findgroup.group_name == new_group_name
	# 		return True
	# return False
    #
    # def update_group_user(self, management, group_id : int, user_id, management: management):
	# user = management.get_user(user_id)
	# if user:
	# 	return management.delete_group_member(group_id, user_id)
	# else
	# 	return management.add_group_memeber(group_id, user_id)
    #
    # def create_announcement(self, user_id: str,group_id: int, postname: str,content: str,  management: management):
	# return management.create_announcement(self.user_id, group_id, postname, content)
    #
    # def delete_announcement(self, group_id: int, post_id : int, management: management)
	# return management.delete_announcement(group_id, post_id)
    #
    # def update_announcement(self, group_id: int, post_id : int, postname : str, content : str, management):
	# return management.update_announcement(group_id, post_id, postname, content)
    #
    #
    #
    # def delete_announcement_comment(self, group_id, post_id, comment_id, management):
	# return management.delete_announcement_comment(group_id, post_id, comment_id)
    #
    # def delete_debate_comment(self, group_id, post_id, comment_id, management):
	# return management.delete_debate_comment(group_id, post_id, comment_id):
    #
