# 230403 오답
def solution(n, k, enemy):
    cnt = 0
    
    for i in range(len(enemy)) :
        if n >= enemy[i] :
            cnt += 1
            n -= enemy[i]
        else :
            if k != 0 :
                k -= 1
                cnt += 1
            else :
                break
    return cnt