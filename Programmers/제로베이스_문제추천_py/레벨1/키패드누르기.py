def solution(numbers, hand):
    answer = ''
    keypad = {1:(0,0), 2:(0,1), 3:(0,2), 
              4:(1,0), 5:(1,1), 6:(1,2),
              7:(2,0), 8:(2,1), 9:(2,2),
              '*':(3,0), 0:(3,1), '#':(3,2)}
    left = keypad['*']
    right = keypad['#']
    
    
    for n in numbers :
        if n == 1 or n == 4 or n == 7 :
            left = keypad[n]
            answer += "L"
        
        elif n == 3 or n == 6 or n == 9 :
            right = keypad[n]
            answer += "R"
        
        else :
            if abs(left[0] - keypad[n][0]) + abs(left[1] - keypad[n][1]) < abs(right[0] - keypad[n][0]) + abs(right[1] - keypad[n][1]) :
                left = keypad[n]
                answer += "L"
            
            elif abs(left[0] - keypad[n][0]) + abs(left[1] - keypad[n][1]) > abs(right[0] - keypad[n][0]) + abs(right[1] - keypad[n][1]) :
                right = keypad[n]
                answer += "R"
        
            else :
                if hand == "left" :
                    left = keypad[n]
                    answer += "L"
                else :
                    right = keypad[n]
                    answer += "R"
            
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))