def solution(n):
    answer = 0
    lists = []
    for i in range(1, n+1) :
        if n % i == 0 :
            lists.append(i)
    
    answer = len(lists)
    return answer