import sys

alphabet_write_cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
type_and_cnt = {}

for i in range(65, 91) :
    type_and_cnt[chr(i)] = alphabet_write_cnt[i-65]

# print(type_and_cnt)
me = list(sys.stdin.readline().rstrip())
her = list(sys.stdin.readline().rstrip())

cnt_list = []
# me와 her의 이름길이는 같다
for i in range(len(me)) :
    cnt_list.append(type_and_cnt[me[i]])
    cnt_list.append(type_and_cnt[her[i]])

while True :
    tmp = []
    for i in range(len(cnt_list)-1) :
        val = cnt_list[i] + cnt_list[i+1]
        tmp.append(int(str(val)[-1]))
    cnt_list = tmp

    if len(cnt_list) == 2 :
        break

print(str(cnt_list[0]) + str(cnt_list[1]))