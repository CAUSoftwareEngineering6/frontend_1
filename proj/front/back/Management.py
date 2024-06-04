from .Debate import *
from .Announcement import *
from .Comment import *
from .Group import *
from .User import *
from .StudentAndProfessor import *
from .MockDatabase import MockDatabase

class Management:
    def __init__(self, database = MockDatabase(), Usercapacity = 100):
        self.database = database
        self.Usercapacity = Usercapacity

    def check_capacity(self):
        return len(self.database.users) > self.Usercapacity

    def get_user(self, user_id):
        for user in self.database.users:
            if user.student_id == user_id:
                return user
        return None



    def create_user(self, user_id: str, username: str, password: str, email: str, gender: str):
        if not self.check_capacity():
            new_user = User(user_id, username, password, email, gender)
            self.database.users.append(new_user)
            return True
        return False

    def delete_user(self, user_id: str):
        deluser = self.get_user(user_id)
        if deluser is not None:
            for group in self.database.groups:
                if deluser in group.members:
                    group.members.remove(deluser)
            self.database.users.remove(deluser)
            return True
        return False

    def get_user_by_name(self, username: str):
        matched = []
        for user in self.database.users:
            if user.username == username:
                matched.append(user)
        return matched if matched else None

    def get_user_by_id(self, personal_id: int):
        matched = []
        for user in self.database.users:
            if isinstance(user, Student) and user.student_id == personal_id:
                matched.append(user)
            elif isinstance(user, Professor) and user.professor_id == personal_id:
                matched.append(user)
        return matched if matched else None

    def show_user(self, searching=None):
        if searching is None:
            return [user.to_dict() for user in self.database.users]
        else:
            by_id = self.get_user_by_id(searching)
            by_name = self.get_user_by_name(searching)
            result = []
            if by_id:
                result.extend([user.to_dict() for user in by_id])
            if by_name:
                result.extend([user.to_dict() for user in by_name])
            return result

    def show_user_detail(self, current_user_id, user_id):
        current_user = self.get_user(current_user_id)
        user = self.get_user(user_id)
        if not user or not current_user:
            return None
        elif isinstance(current_user, Professor):
            if isinstance(user, Student):
                return user.get_detail(user_id)
            else:
                return user.to_dict()
        elif isinstance(current_user, Student):
            if isinstance(user, Student):
                return user.get_detail(current_user_id)
            elif isinstance(user, Professor):
                return {
                    "user_id": user.user_id,
                    "username": user.username,
                    "email": user.email,
                    "gender": user.gender,
                    "profileImage": user.profileImage,
                    "professor_id": user.professor_id
                }
        else:
            return user.to_dict()

    # ----------------------------------- 그룹 메서드 ------------------------------------
    def show_group(self, user_id, group_name=None, user_name=None):
        if group_name is None and user_name is None:
            return_list = []
            for group in self.database.groups:
                return_list.append({'group_id' : group.group_id, 'group_name' : group.group_name,'member_num' : len(group.members), 'accessible' : group.check_user_access(user_id)})
            return return_list
        elif group_name is not None:
            return_list = []
            for group in self.database.groups:
                if group_name == group.group_name:
                    return_list.append({'group_id' : group.group_id, 'group_name': group.group_name, 'member_num': len(group.members),
                                        'accessible': group.check_user_access(user_id)})
                    break
            return return_list
        elif user_name is not None:
            return_list = []
            for group in self.database.groups:
                if user_name in group.members:
                    return_list.append({'group_id' : group.group_id, 'group_name': group.group_name, 'member_num': len(group.members),
                                        'accessible': group.check_user_access(user_id)})
                    break
            return return_list





    def create_group(self, group_id: str, group_name: str):
        new_group = Group(group_id, group_name)
        self.database.groups.append(new_group)
        return True

    def delete_group(self, group_id: str):
        group = self.database.search_group(group_id)
        self.database.groups.remove(group)
        return True

    def add_group_member(self, group_id: str, user_id: str):
        group = self.database.search_group(group_id)
        user = self.database.search_user(user_id)
        if group and user:
            group.add_member(user)
            return True
        else:
            return False

    def delete_group_member(self, group_id: str, user_id: str):
        group = self.database.search_group(group_id)
        user = self.database.search_user(user_id)
        if group and user:
            group.delete_member(user)
            return True
        else:
            return False

    def show_debate(self, group_id):
        group = self.database.search_group(group_id)
        debate_list = []
        for debate in group.debates:
            comment_list = []
            for comment in debate.comments:
                comment_list.append({'comment_id' : comment.comment_id, 'comment_username' : comment.writer.username, 'comment_content' : comment.content, 'created_at' : comment.created_at})
            debate_list.append({'post_id': debate.post_id, "writer_name" : debate.writer.username, "post_name" : debate.postname, 'comment_list': comment_list, 'created_at' : debate.created_at})
        return debate_list

    def show_announcement(self, group_id):
        group = self.database.search_group(group_id)
        announcement_list = []
        for announcement in group.announcements:
            comment_list = []
            for comment in announcement.comments:
                comment_list.append({'comment_id' : comment.comment_id, 'comment_username' : comment.writer.username, 'comment_content' : comment.content, 'created_at' : comment.created_at})
            announcement_list.append({'post_id': announcement.post_id,'writer_name' :  announcement.writer.username, 'post_name' : announcement.postname, 'content' : announcement.content, 'comment_list' : comment_list, 'created_at' : announcement.created_at})
        return announcement_list

    def create_debate(self, user_id, group_id, postname):
        group = self.database.search_group(group_id)
        member = group.search_menber(user_id)
        if group and member:
            new_debate = Debate(member, postname)
            group.add_debate(new_debate)
            return True
        return False

    def delete_debate(self, group_id, post_id):
        group = self.database.search_group(group_id)
        debate = group.search_debate(post_id)
        if group and debate:
            group.debates.remove(debate)
            return True
        return False

    def update_debate(self, group_id, post_id, postname):
        group = self.database.search_group(group_id)
        debate = group.search_debate(post_id)
        if group and debate:
            debate.update_postname(postname)
            return True
        return False

    def create_announcement(self, user_id, group_id, postname, content):
        group = self.database.search_group(group_id)
        member = group.search_menber(user_id)
        if group and member:
            new_announcement = Announcement(member, postname, content)
            group.add_announcement(new_announcement)
            return True
        return False

    def delete_announcement(self, group_id, post_id):
        group = self.database.search_group(group_id)
        announcement = group.search_announcement(post_id)
        if group and announcement:
            group.announcements.remove(announcement)
            return True
        return False

    def update_announcement(self, group_id, post_id, postname, content):
        group = self.database.search_group(group_id)
        announcement = group.search_announcement(post_id)
        if group and announcement:
            announcement.update_postname(postname, content)
            return True
        return False

    def create_debate_comment(self, user_id, group_id, post_id, content):
        group = self.database.search_group(group_id)
        debate = group.search_debate(post_id)
        member = group.search_menber(user_id)
        new_comment = Comment(member, content)
        if group and debate and member:
            debate.create_comment(new_comment)
            return True
        return False

    def create_announcement_comment(self, user_id, group_id, post_id, content):
        group = self.database.search_group(group_id)
        announcement = group.search_announcement(post_id)
        member = group.search_menber(user_id)
        new_comment = Comment(member, content)
        if group and announcement and member:
            announcement.create_comment(new_comment)
            return True
        return False

    def delete_debate_comment(self, group_id, post_id, comment_id):
        group = self.database.search_group(group_id)
        debate = group.search_debate(post_id)
        comment = debate.search_comment(comment_id)
        if group and debate and comment:
            debate.delete_comment(comment)
            return True
        return False

    def delete_announcement_comment(self, group_id, post_id, comment_id):
        group = self.database.search_group(group_id)
        announcement = group.search_announcement(post_id)
        comment = announcement.search_comment(comment_id)
        if group and announcement and comment:
            announcement.delete_comment(comment)
            return True
        return False

    def update_debate_comment(self, group_id, post_id, comment_id, content):
        group = self.database.search_group(group_id)
        debate = group.search_debate(post_id)
        comment = debate.search_comment(comment_id)
        if group and debate and comment:
            debate.update_comment(comment, content)
            return True
        return False

    def update_announcement_comment(self, group_id, post_id, comment_id, content):
        group = self.database.search_group(group_id)
        announcement = group.search_announcement(post_id)
        comment = announcement.search_comment(comment_id)
        if group and announcement and comment:
            announcement.update_comment(comment, content)
            return True
        return False



