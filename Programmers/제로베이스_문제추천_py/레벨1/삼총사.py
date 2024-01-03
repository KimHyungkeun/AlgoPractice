def solution(number):
    answer = 0
    visited = []
    for i in range(len(number)) :
        for j in range(len(number)) :
            if i == j :
                continue
            for k in range(len(number)) :
                if j == k or i == k:
                    continue
                if number[i] + number[j] + number[k] == 0 and [i,j,k] not in visited:
                    visited.append([i,j,k])
                    answer += 1
            
    for i in range(len(visited)) :
        visited[i].sort()
        visited[i] = tuple(visited[i])
    
    answer = len(set(visited))
    return answer