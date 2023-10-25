# 정답코드 : 힌트는 원의 방정식
def solution(k, d):
    answer = 0
    pos = []
    
    for x in range(0, d+1, k) :
        y = (d**2 - x**2)**0.5
        answer += (y // k) + 1

    
    return answer

# 아래는 시간초과
def solution(k, d):
    answer = 0
    pos = []
    for i in range(d+1) :
        if i*k <= d :
            pos.append(i*k)
    
    for num in pos :
        for n in pos :
            if (num**2 + n**2)**0.5 <= d :
                answer += 1
            else :
                break
    
    return answer