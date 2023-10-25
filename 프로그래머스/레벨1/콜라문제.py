def solution(a, b, n):
    answer = 0

    while n >= a:
        empty = n % a
        coke = (n // a) * b

        answer += coke
        n = empty + coke

    return answer
