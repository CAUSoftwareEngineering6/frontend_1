from .Management import Management


M = Management()


print('show_user 테스트')
print(M.show_user())
print('\nshow_user 학번 검색 테스트')
print(M.show_user("학번1"))
print('\nshow_user 이름 검색 테스트')
print(M.show_user("user2"))

print('\ncreate_user 테스트')
M.create_user("5", "user4", "1234", "user4@cau.ac.kr", "female")
print(M.show_user())

print('\ndelete_user 테스트')
M.delete_user("5")
print(M.show_user())

print('\nshow_user_detail 테스트: 1 자기 자신 2 다른 사람')
print(M.show_user_detail("1","1"))
print(M.show_user_detail("20192115","20192115"))
print(M.show_user_detail("1","2"))


print('\nshow_group 테스트')
print(M.show_group("1"))

print(M.create_group("4", "4조"))
print(M.show_group("1"))

print(M.delete_group("4"))
print(M.show_group("1"))


print('add_group_member 테스트')
print(M.show_group("1", "Group1"))
print(M.add_group_member("1", "1"))
print(M.show_group("1", "Group1"))
print('')

print('delete_group_member 테스트')
print(M.show_group("1", "Group1"))
print(M.delete_group_member("1", "1"))
print(M.show_group("1", "Group1"))
print('')

print('show_debate 테스트')
print(M.show_debate("1"))
print('')

print('show_announcement 테스트')
print(M.show_announcement("1"))

print('show_debate 테스트')
print(M.show_debate("1"))
print('')

print('create_debate 테스트')
print(M.show_debate("1"))
print(M.create_debate("1", "1", "새로운 토론"))
print(M.show_debate("1"))
print('')

print('create_announcement 테스트')
print(M.show_announcement("1"))
print(M.create_announcement("1", "1", "새로운 공지 제목", "새로운 공지 내용"))
print(M.show_announcement("1"))
print('')



print('delete_debate 테스트')
print(M.show_debate("1"))
print(M.delete_debate("1", "1"))
print(M.show_debate("1"))
print('')

print('delete_announcement 테스트')
print(M.show_announcement("1"))
print(M.delete_announcement("1", "1"))
print(M.show_announcement("1"))
print('')


print('create_debate_comment 테스트')
print(M.show_debate("1"))
print(M.create_debate_comment("1", "1", "3", "새로운 댓글"))
print(M.show_debate("1"))
print('')

print('create_announcement_comment 테스트')
print(M.show_announcement("1"))
print(M.create_announcement_comment("1", "1", "3", "새로운 댓글"))
print(M.show_announcement("1"))
print('')


print('update_announcement_comment 테스트')
print(M.show_announcement("1"))
print(M.update_announcement_comment("1", "3", "4", "갱신된 댓글"))
print(M.show_announcement("1"))
print('')


print('delete_announcement_comment 테스트')
print(M.show_announcement("1"))
print(M.delete_announcement_comment("1", "3", "4"))
print(M.show_announcement("1"))
print('')

