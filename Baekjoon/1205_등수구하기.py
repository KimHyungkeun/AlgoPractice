# 230907 Retry Success
import sys

n, taesu, p = map(int, sys.stdin.readline().split())

if n == 0 :
    print(1)

else :
    score_list = list(map(int, sys.stdin.readline().split()))

    rank = 1
    score_with_rank = []
    for s in score_list :
        if not score_with_rank :
            score_with_rank.append([s, rank])
        else :
            if score_with_rank[-1][0] == s :
                score_with_rank.append(score_with_rank[-1])
            else :
                score_with_rank.append([s, rank])
        rank += 1

    while score_with_rank and score_with_rank[-1][0] < taesu :
        score_with_rank.pop()
    
    taesu_rank = 1
    if score_with_rank : 
        if score_with_rank[-1][0] > taesu :
            taesu_rank = len(score_with_rank) + 1
        else :
            taesu_rank = score_with_rank[-1][1]

    score_with_rank.append([taesu, taesu_rank])

    if len(score_with_rank) > p :
        print(-1)
    else :
        print(score_with_rank[-1][1])

# # 230717 19%에서 오답
# # 230820 정답
# import sys

# n, taesu_score, p = map(int, sys.stdin.readline().split())

# if n == 0 :
#     print(1)

# else :
#     stack = []
#     rank = 1
#     score_list = list(map(int, sys.stdin.readline().split()))
   
#     # score list의 점수를 맨 왼쪽부터 시작하여 stack에 삽입
#     for s in score_list :
#         if not stack :
#             stack.append([s, rank])
#         else :
#             if stack[-1][0] == s :
#                 stack.append([s, stack[-1][1]])
#             else :
#                 stack.append([s, rank])
#         rank += 1
    
#     # 태수의 랭크는 일단 가장 맨 끝 랭크라고 가정한다
#     taesu_recent_rank = rank
#     while stack :
#         if stack[-1][0] < taesu_score :
#             info = stack.pop()
#             taesu_recent_rank = info[1]
#         else :
#             break

#     # 가장 하위 랭킹부터 시작하여, 태수의 랭킹이 어느정도인지 하나씩 확인해 본다
#     # 만약 태수가 기 등록된 점수들을 갱신하였을때, 태수 가장 바로 윗랭킹 점수와 같으면, 태수도 바로 윗랭킹과 공동 순위를 가진다 
#     if stack :
#         if stack[-1][0] == taesu_score :
#             stack.append([taesu_score, stack[-1][1]])
#         else :
#             stack.append([taesu_score, taesu_recent_rank])
#     else :
#         stack.append([taesu_score, 1])

#     if len(stack) > p :
#         print(-1)   
#     else :
#         print(stack[-1][1])
    