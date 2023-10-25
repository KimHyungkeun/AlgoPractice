def solution(sides):
    answer = 0
    sides.sort(reverse=True)
    
    for i in range(sides[0], 0, -1) :
        if sides[0] < sides[1] + i :
            answer += 1
        else :
            break
    
    for i in range(sides[0] + sides[1] - 1, sides[0], -1) :
        answer += 1
    
    return answer