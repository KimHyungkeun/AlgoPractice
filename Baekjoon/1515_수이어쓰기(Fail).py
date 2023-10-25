import sys

# n = sys.stdin.readline().rstrip()
n = '9'*1000
num_str = ''
num_list = []
num = 1

# 숫자들을 1~n까지 나열한 숫자문자열을 정의하고, 또한 숫자들을 차례대로 정리한 리스트까지 정의한다
while len(num_str) <= 3000 :
    num_str += str(num)
    num_list.append(str(num))
    num += 1

# 숫자문자열 기준으로, 입력한 n의 가장 끝자리가 몇번째 idx인지 구한다
idx = 0
for pos in n :
    while idx < 3000 :
        if num_str[idx] == pos :
            idx += 1
            break
        idx += 1 
    

tmp = []
idx -= 1
str_len = 0
num_list_i = 0
while True :
    str_len += len(num_list[num_list_i])
    tmp.append(num_list[num_list_i])
    if str_len > idx :
        break
    num_list_i += 1
    
print(tmp[-1])