# 230515 재풀이
import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n) :
    string = sys.stdin.readline().rstrip()
    alpha_redency = {}
    flag = True
    set_zero = False

    for i in range(len(string)) :
        if set_zero :
            set_zero = False
            continue
        if string[i] not in alpha_redency :
            alpha_redency[string[i]] = 1
        else :
            alpha_redency[string[i]] += 1

        if alpha_redency[string[i]] == 3 :
            if i == len(string)-1 or string[i] != string[i+1] : 
                flag = False
                break
            else :
                alpha_redency[string[i]] = 0
                set_zero = True

    if not flag :
        print("FAKE")
    else :
        print("OK")


# 이전 답안 (반례를 보고 확인)
# import sys
# n = int(sys.stdin.readline().rstrip())
# for _ in range(n) :
#     frequency = {}
#     flag = True
#     m = sys.stdin.readline().rstrip()

#     # 문자 별로 등장빈도가 3번째 등장인 타이밍 때, 그 뒤 문자가 한번 더 적혀져야 한다. 
#     # 그렇지 않으면 FAKE 문서
#     for i in range(len(m)) :
#         if m[i] not in frequency :
#             frequency[m[i]] = 1
#         else :
#             frequency[m[i]] += 1
        
#         if frequency[m[i]] == 4 :
#             frequency[m[i]] = 0
#             continue
        
#         if frequency[m[i]] == 3 :
#             if i == len(m)-1 :
#                 flag = False
#                 break
#             if m[i] != m[i+1] :
#                 flag = False
#                 break 
        
    
#     if flag :
#         print("OK")
#     else :
#         print("FAKE")