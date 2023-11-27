#정답참고 : https://deftkang.tistory.com/175
from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)) :
        sec = 0
        for j in range(i+1, len(prices)) :
            if prices[i] <= prices[j] :
                answer[i] += 1
            else :
                answer[i] += 1
                break
    
    print(answer)
    return answer
    # answer = deque([])
    # q = deque([])
    # min_pos= 0

    # while prices :
    #     print(prices, q, answer)
    #     if not q :
    #         q.appendleft(prices.pop())
    #         answer.appendleft(min_pos)
    #     else :
    #         if prices and prices[-1] > q[0] :
    #             q.appendleft(prices.pop())
    #             min_pos = 1
    #             answer.appendleft(min_pos)
                
    #         else :
    #             q.appendleft(prices.pop())
    #             min_pos += 1
    #             answer.appendleft(min_pos)
                


    # print(answer)
    # return answer

# prices = [1,2,3,2,3]
prices = [1,2,3,3,3,2,3]
solution(prices)