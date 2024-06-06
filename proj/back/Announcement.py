from .Post import Post

class Announcement(Post):
    next_id = 1

    def __init__(self, writer, postname: str, content: str):
        super().__init__(writer, postname)
        self.post_id = str(Announcement.next_id)
        Announcement.next_id += 1
        self.content = content

    def delete_post(self):
        self.content = ""

    def update_content(self, new_postname: str, new_content: str):
        self.postname = new_postname
        self.content = new_content
