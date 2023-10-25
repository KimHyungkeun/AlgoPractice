# 20230218 정답
import heapq
def solution(numbers):
    answer = [-1] * len(numbers)
    heap = []
    for i in range(len(numbers)) :
        
        while heap and heap[0][0] < numbers[i] :
            val, idx = heapq.heappop(heap)
            answer[idx] = numbers[i]
        heapq.heappush(heap, (numbers[i], i))
    
    return answer
# 참고 : https://school.programmers.co.kr/questions/43218

# 20230218 시간초과 코드
from collections import deque
def solution(numbers):
    answer = []
    idx = 0
    
    q = deque(numbers)

    while q :
        val = q.popleft()
        flag = False
        
        for n in q :
            if val < n :
                answer.append(n)
                flag = True
                break
        if not flag :
            answer.append(-1)
    
    
    return answer