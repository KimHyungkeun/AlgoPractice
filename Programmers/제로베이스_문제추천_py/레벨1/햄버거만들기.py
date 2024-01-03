def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient :
        if not stack :
            stack.append(i)
        else :
            if len(stack) >= 4 :
                if stack[-4] == 1 and stack[-3] == 2 and stack[-2] == 3 and stack[-1] == 1 :
                    for _ in range(4) :
                        stack.pop()
                    answer += 1             
                stack.append(i)
            else : 
                stack.append(i)
    
    if len(stack) >= 4 :
            if stack[-4] == 1 and stack[-3] == 2 and stack[-2] == 3 and stack[-1] == 1 :
                answer += 1
    return answer