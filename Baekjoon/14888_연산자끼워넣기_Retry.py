# 정답코드
# https://data-flower.tistory.com/72
import sys

# 수의 갯수 입력
n = int(sys.stdin.readline().rstrip())

# 수열 입력 받기
data = list(map(int, sys.stdin.readline().split()))

# 연산자 갯수 계산
add, sub, mul, div = map(int, sys.stdin.readline().split())

# 최댓값과 최솟값 초기화
max_val = -1e9
min_val = 1e9

def dfs(i ,arr) :
    global add, sub, mul, div, max_val, min_val
    # 주어진 수열을 다 밟았을 경우 최댓값과 최솟값 계산
    if i == n :
        max_val = max(max_val, arr)
        min_val = min(min_val, arr)
    else :
        # 더하기
        if add > 0 :
            add -= 1
            dfs(i+1, arr + data[i])
            add += 1
        # 빼기
        if sub > 0 :
            sub -= 1
            dfs(i+1, arr - data[i])
            sub += 1
        # 곱셈
        if mul > 0 :
            mul -= 1
            dfs(i+1, arr * data[i])
            mul += 1
        # 나눗셈
        if div > 0 :
            div -= 1
            dfs(i+1, int(arr / data[i]))
            div += 1

dfs(1, data[0])

print(int(max_val))
print(int(min_val))

# 231025 3번째 예제 틀림
# import sys

# n = int(sys.stdin.readline().rstrip())

# num_list = list(map(int, sys.stdin.readline().split()))

# operator_dict = {}
# operator_cnt = list(map(int, sys.stdin.readline().split()))

# for idx in range(len(operator_cnt)) :
#     if operator_cnt[idx] == 0 :
#         continue
#     if idx == 0 :
#         operator_dict['+'] = operator_cnt[idx]
#     if idx == 1 :
#         operator_dict['-'] = operator_cnt[idx]
#     if idx == 2 :
#         operator_dict['*'] = operator_cnt[idx]
#     if idx == 3 :
#         operator_dict['//'] = operator_cnt[idx]

# candidate_list = []

# graph = {}
# for i in range(n) :
#     if i == n-1 :
#         graph[num_list[i]] = 0
#     else :
#         graph[num_list[i]] = num_list[i+1]


# def oper(operator, start_val, next_val) :
    
#     if operator == '+' :
#         total_val = start_val + next_val
#     if operator == '-' :
#         total_val = start_val - next_val
#     if operator == '*' :
#         total_val = start_val * next_val
#     if operator == '//' :
#         if next_val == 0 :
#             total_val = 0
#         else :
#             total_val = int(start_val / next_val)
#     operator_dict[operator] -= 1

    
#     if sum(operator_dict.values()) == 0 or next_val == 0 :
#         candidate_list.append(total_val)
#         operator_dict[operator] += 1
#         return

#     if '+' in operator_dict and operator_dict['+'] != 0 :
#         oper('+', total_val, graph[next_val])
        
#     if '-' in operator_dict and operator_dict['-'] != 0 :
#         oper('-', total_val, graph[next_val])
        
#     if '*' in operator_dict and operator_dict['*'] != 0 :
#         oper('*', total_val, graph[next_val])
        
#     if '//' in operator_dict and operator_dict['//'] != 0 :
#         oper('//', total_val, graph[next_val])
    
#     operator_dict[operator] += 1

# if '+' in operator_dict :
#     oper('+', num_list[0], graph[num_list[0]])
# if '-' in operator_dict :
#     oper('-', num_list[0], graph[num_list[0]])
# if '*' in operator_dict :
#     oper('*', num_list[0], graph[num_list[0]])
# if '//' in operator_dict :
#     oper('//', num_list[0], graph[num_list[0]])

# print(max(candidate_list))
# print(min(candidate_list))