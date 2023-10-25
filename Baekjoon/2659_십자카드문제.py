# 230627 문제의 예시 이해가 안되서 블로그 찾아봄
import sys

num_list = list(map(int, sys.stdin.readline().split()))

num_case = []
for i in range(4) :
    tmp = ""
    for j in range(i, i+4) :
        tmp += str(num_list[j%4])
    num_case.append(int(tmp))

min_num = min(num_case)


# 가장 최소의 십자수 1111부터 시작하여, min_num이 몇번째 십자수인지 구한다
# 단, 십자수중에 0은 포함되면 안된다 (1부터 9까지의 숫자만 가능하므로)
visited = set([])
cnt = 0

for n in range(1111, min_num+1) :
    str_list = list(str(n))

    if '0' in str_list :
        continue
    
    cross_num = []
    for i in range(4) :
        tmp = ""
        for j in range(i, i+4) :
            tmp += str(str_list[j%4])
        cross_num.append(tmp)

    if int(cross_num[0]) > min_num :
            continue

    if cross_num[0] not in visited :
        for c in cross_num :
             visited.add(c)
        cnt += 1


print(cnt)
