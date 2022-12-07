from itertools import combinations


def solution(number):
    answer = 0

    triple = list(combinations(number, 3))

    for t in triple:
        if sum(t) == 0:
            answer += 1
    return answer
