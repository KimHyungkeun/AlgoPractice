from collections import deque
def solution(prices):
    answer = deque([])
    q = deque([])
    min_pos= 0

    while prices :
        if not q :
            q.appendleft(prices.pop())
            answer.appendleft(0)
        else :
            if prices[-1] <= q[0] :
                q.appendleft(prices.pop())
                answer.append(min_pos)
                min_pos = 0
            else :
                min_pos += 1



    return answer

prices = [1,2,3,2,3]
solution(prices)