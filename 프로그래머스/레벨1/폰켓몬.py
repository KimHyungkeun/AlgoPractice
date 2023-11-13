def solution(nums):
    answer = 0
    half = len(nums) // 2
    
    num_sets = list(set(nums))
    
    if len(num_sets) > half :
        answer = half
    else :
        answer = len(num_sets)
        
    return answer