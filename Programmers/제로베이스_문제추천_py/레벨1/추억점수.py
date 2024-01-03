def solution(name, yearning, photo):
    answer = []
    memory_dict = {}
    for i in range(len(name)) :
        memory_dict[name[i]] = yearning[i]
    
    for p in photo :
        total = 0
        for n in p :
            if n in memory_dict :
                total += memory_dict[n]
        answer.append(total)
    return answer