def solution(quiz):
    answer = []
    for q in quiz :
        sentence = q.split()
        if sentence[1] == '-' :
            if int(sentence[0]) - int(sentence[2]) == int(sentence[-1]):
                answer.append("O")
            else : 
                answer.append("X")
        
        if sentence[1] == '+' : 
            if int(sentence[0]) + int(sentence[2]) == int(sentence[-1]):
                answer.append("O")
            else : 
                answer.append("X")
          
    return answer