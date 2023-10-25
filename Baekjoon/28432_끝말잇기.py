import sys

n = int(sys.stdin.readline().rstrip())
word_list = []
for _ in range(n) :
    word_list.append(sys.stdin.readline().rstrip())

m = int(sys.stdin.readline().rstrip())
candidate_list = []
for _ in range(m) :
    candidate_list.append(sys.stdin.readline().rstrip())

question_idx = word_list.index('?')


# 구하고자 하는 단어가 맨 앞쪽에 있을 때
# 만약 끝말잇기에 기입된 기록이 하나밖에 없다면 후보단어중 가장 첫번째 단어를 선택
if question_idx == 0 :
    if len(word_list) == 1 :
        print(candidate_list[0])
    else :
        end_spell = word_list[1][0]
        for c in candidate_list :
            if c[-1] == end_spell and c not in word_list :
                break
        print(c)

# 구하고자 하는 단어가 맨 뒷쪽에 있을 때
elif question_idx == n-1 :
    start_spell = word_list[n-2][-1]
    for c in candidate_list :
        if c[0] == start_spell and c not in word_list :
            break
    print(c)

# 구하고자 하는 단어가 양 단어 사이에 있을 때
else :
    start_spell = word_list[question_idx-1][-1]
    end_spell = word_list[question_idx+1][0]
    for c in candidate_list :
        if c[0] == start_spell and c[-1] == end_spell and c not in word_list :
            break
    print(c)

