import sys

n = int(sys.stdin.readline().rstrip())

cnt = 0
user_list = set([])
for _ in range(n) :
    chat = sys.stdin.readline().rstrip()
    if chat == 'ENTER' :
        user_list = set([])
    else :
        before_len = len(user_list)
        user_list.add(chat)
        after_len = len(user_list)

        if before_len < after_len :
            cnt += 1

print(cnt)


    