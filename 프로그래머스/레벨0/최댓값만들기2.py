def solution(numbers):
    answer = 0
    minus = []
    plus = []

    for n in numbers:
        if n < 0:
            minus.append(n)
        else:
            plus.append(n)

    minus.sort(reverse=True)
    plus.sort(reverse=True)

    if len(plus) >= 2 and len(minus) >= 2:
        answer = max(plus[0]*plus[1], minus[0]*minus[1])
    elif len(plus) >= 2 and len(minus) < 2:
        answer = plus[0]*plus[1]
    elif len(minus) >= 2 and len(plus) < 2:
        answer = minus[0]*minus[1]
    elif len(minus) == 1 and len(plus) == 1:
        answer = minus[0]*plus[0]
    else:
        answer = 0
    return answer
