# 230328 정답
def solution(n, m, section):
    answer = 0
    maximum = 0
    
    for i in range(len(section)) :
        if section[i] < maximum :
            continue
        
        
        maximum = section[i] + m
        answer += 1    
        
    return answer
    
# 정답출처 : https://velog.io/@namkun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-lv2-%EB%8D%A7%EC%B9%A0%ED%95%98%EA%B8%B0
from collections import deque
def solution(n, m, section):
    answer = 0
    maximum = 0
    
    for i in range(len(section)) :
        if section[i] < maximum :
            continue
        
        answer += 1
        maximum = section[i] + m
        
    return answer

n = 4
m = 1
section = [1, 2, 3, 4]
solution(n, m, section)

# 230309 실패
from collections import deque
def solution(n, m, section):
    answer = 0
    q = deque(section)
    
    start = 1
    flag = False
    while q : 
        print(start)
        if start + m > n :
            break
            
        for i in range(start, start+m) :
            if i == q[0] :
                q.popleft()
                flag = True
            if not q :
                break
        if flag :
            answer += 1
        
        flag = False    
        start += 1

        
    return answer

# 230314 실패
from collections import deque
def solution(n, m, section):
    answer = 0
    q = deque(section)
    
    start = 1
    last = 1
    flag = False
    while q : 

        if start + m - 1 > n :
            break
            
        for i in range(start, start+m) :
            if i == q[0] :
                q.popleft()
                last = i
                flag = True
            if not q :
                break
        if flag :
            answer += 1
        
        flag = False    
        start = last+1

    return answer

