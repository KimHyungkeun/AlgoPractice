def solution(box, n):
    answer = 0
    
    width = box[0] // n
    vertical = box[1] // n
    height = box[2] // n
    
    answer = width * vertical * height
    return answer