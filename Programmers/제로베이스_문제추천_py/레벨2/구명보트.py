def solution(people, limit):
    cnt = 0
    left = 0
    right = len(people)-1
    people.sort()
    
    while left <= right :
        if people[left] + people[right] <= limit :
            left += 1
            right -= 1
            cnt += 1
        elif people[left] < people[right] :
            right -= 1
            cnt += 1
        elif people[left] > people[right] :
            left += 1
            cnt += 1
        else :
            left += 1
            cnt += 1
        
        
    
    
# 실패코드
#     while people :
#         ship_weight = 0
#         ship_possible_cnt = 0
        
#         while people and ship_possible_cnt <= 2 and people[-1] + ship_weight <= limit :
#             ship_weight += people.pop()
#             ship_possible_cnt += 1
#         cnt += 1
     
    return cnt