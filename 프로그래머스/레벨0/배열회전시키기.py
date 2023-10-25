from collections import deque
def solution(numbers, direction):
    answer = []
    
    q = deque(numbers)
    
    if direction == 'right' :
        q.appendleft(q.pop())
    else :
        q.append(q.popleft())
    
    answer = list(q)
    return answer