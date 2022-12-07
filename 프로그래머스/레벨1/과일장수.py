def solution(k, m, score):
    answer = 0
    score.sort()

    tmp = []
    while score:
        tmp.append(score.pop())
        if len(tmp) == m:
            answer += (min(tmp) * m)
            tmp = []

    if len(score) == m:
        answer += (min(score) * m)

    return answer
