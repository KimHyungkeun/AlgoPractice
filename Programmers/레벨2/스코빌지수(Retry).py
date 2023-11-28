# 정답코드 (231128)
# https://school.programmers.co.kr/learn/courses/30/lessons/42626/solution_groups?language=python3&type=my
import heapq
def solution(scoville, K):
    answer = 0

    # 비어있는 배열
    heap = []
    for num in scoville :
        heapq.heappush(heap, num)

    # print(heapq.heappop(heap))
    # print(heap)
    while len(heap) > 1 :
        flag = True

        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        mixed = first + (second * 2)
        heapq.heappush(heap, mixed)
        answer += 1

        for n in heap :
            if n < K :
                flag = False
                break

        if flag :
            print(answer)
            return answer

    return -1

# 오답코드 (231128)
# import heapq

# def solution(scoville, K):
#     answer = 0
    

#     while len(scoville) > 1 :
#         flag = True

#         answer += 1
#         first = heapq.heappop(scoville)
#         second = heapq.heappop(scoville)
#         heapq.heappush(scoville, first + (second * 2))

#         for s in scoville :
#             if s < K :
#                 flag = False
#                 break
        
#         if flag :
#             break
        

#     if flag :
#         return answer
#     else :
        return -1
        

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))