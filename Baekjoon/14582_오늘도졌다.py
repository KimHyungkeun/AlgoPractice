import sys

jeminis = list(map(int, sys.stdin.readline().split()))
gulibus = list(map(int, sys.stdin.readline().split()))

jeminis_score = 0
gulibus_score = 0

win_state_list = []
win_state = False
for i in range(9) :
    jeminis_score += jeminis[i]
    if jeminis_score > gulibus_score :
        win_state = True
    win_state_list.append(win_state)

    gulibus_score += gulibus[i]
    if jeminis_score < gulibus_score :
        win_state = False
    win_state_list.append(win_state)

# 역전한 구간이 한번이라도 있는 상태에서 패했다면, 역전패이다
if True in win_state_list :
    print("Yes")
else :
    print("No")


    
        
    
        