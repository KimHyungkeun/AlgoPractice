def solution(rank, attendance):
    answer = 0
    students = []
    for i in range(len(rank)) :
        if attendance[i] :
            students.append((rank[i],i))
    
    students.sort(key = lambda x : x[0])
    answer = 10000 * students[0][1] + 100 * students[1][1] + students[2][1]
    return answer