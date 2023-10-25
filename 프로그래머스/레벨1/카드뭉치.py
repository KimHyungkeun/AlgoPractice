from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    q1 = deque(cards1)
    q2 = deque(cards2)
    
    for g in goal :
        if q1 and g == q1[0] :
            q1.popleft()
        elif q2 and g == q2[0] :
            q2.popleft()
        else :
            answer = 'No'
            break
    
    return answer