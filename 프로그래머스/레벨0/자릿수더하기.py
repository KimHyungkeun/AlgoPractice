def solution(n):
    answer = 0
    n = list(str(n))
    for val in n :
        answer += int(val)
    return answer