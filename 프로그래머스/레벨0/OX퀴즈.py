def solution(quiz):
    answer = []
    
    for q in quiz :
        lists = q.split()
        if lists[1] == '+' :
            if int(lists[0]) + int(lists[2]) == int(lists[4]) :
                answer.append("O")
            else :
                answer.append("X")
        else :
            if int(lists[0]) - int(lists[2]) == int(lists[4]) :
                answer.append("O")
            else :
                answer.append("X")
            
    return answer