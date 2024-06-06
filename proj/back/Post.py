from datetime import datetime
from typing import List
from .Comment import Comment

class Post:

    def __init__(self, writer, postname: str):
        self.writer = writer
        self.postname = postname
        self.comments: List[Comment] = []
        self.created_at = str(datetime.now())

    def create_comment(self, comment: Comment):
        self.comments.append(comment)

    def delete_comment(self, comment: Comment):
        self.comments.remove(comment)

    def update_comment(self, comment: Comment, new_content: str):
        comment.content = new_content

    def search_comment(self, comment_id):
        for comment in self.comments:
            if comment_id == comment.comment_id:
                return comment




