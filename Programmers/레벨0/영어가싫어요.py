def solution(numbers):
    answer = 0
    ans_str = ''
    num_dict = { "one" : "1", "two" : "2", "three" : "3", "four" : "4",
               "five" : "5", "six" : "6", "seven" : "7", "eight" : "8",
               "nine" : "9", "zero" : "0"}
    
    tmp = ""
    for n in numbers :
        tmp += n
        if tmp in num_dict :
            ans_str += num_dict[tmp]
            tmp = ""
    
    answer = int(ans_str)
    return answer