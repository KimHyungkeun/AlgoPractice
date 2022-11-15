from collections import deque


def solution(A, B):

    if A == B:
        return 0

    right_q = deque(list(A))
    right_result = 0

    for _ in range(len(right_q)):
        right_q.appendleft(right_q.pop())
        right_result += 1
        if ''.join(list(right_q)) == B:
            break

    if right_result == len(right_q):
        result = -1
    else:
        result = right_result
    return result
