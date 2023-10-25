import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
word_group = {}
word_list = []

for _ in range(n) :
    word = sys.stdin.readline().rstrip()
    word_list.append(word)

cnt = 0
while word_list :
    spell_list = list(word_list[0])
    q = deque(spell_list)
    word_type = []

    for _ in range(len(spell_list)) :
        word_type.append(''.join(list(q)))
        q.append(q.popleft())

    idx = 0
    while idx < len(word_list) :
        if word_list[idx] in word_type :
            word_list.remove(word_list[idx])
            idx = 0
        else :
            idx += 1
    
    
    cnt += 1

print(cnt)   

