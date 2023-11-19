#230129 오답

# def solution(storey):
#     answer = 0
#     origin = storey
    
#     unit = 1
#     for i in range(len(str(storey))-1, 0, -1) :
#         # print("자릿수 : ", int(str(storey)[i]))
#         if '0' <= str(storey)[i] <= '4' :
#             answer += int(str(storey)[i])
#             # print("answer", (10 - int(str(storey)[i])))
#             # print("storey", (10 - int(str(storey)[i]) * unit))
#             storey -= (int(str(storey)[i]) * unit)
#         elif '6' <= str(storey)[i] <= '9' :
#             # print("b")
#             answer += (10 - int(str(storey)[i]))
#             # print("answer", (10 - int(str(storey)[i])))
#             # print("storey", (10 - int(str(storey)[i]) * unit))
#             storey += ((10 - int(str(storey)[i])) * unit)
#         else :         
#             if '0' <= str(storey)[i-1] <= '4' :
#                 answer += 5
#                 storey -= (5 * unit)
#             else :
#                 answer += 5
#                 storey += (5 * unit)
        
#         unit *= 10
#         # print(storey)
                
#     # print(storey)
#     print("Before", answer)
#     if '0' <= str(storey)[0] <= '4' :
#         print(storey)
#         tmp = int(str(storey)[0])
#         storey -= tmp * unit
#         answer += tmp
#     else :
#         print(storey)
#         tmp = (10 - int(str(storey)[0]))
#         storey += tmp * unit
#         print("absd", storey)
#         answer += int(str(storey)[0])

#     print("After", answer)
#     return answer

#230130 정답
def solution(storey):
    answer = 0
    origin = storey
    
    unit = 1
    origin_length = len(str(storey))
    i = len(str(storey))-1
    while i > 0 :
        if '0' <= str(storey)[i] <= '4' :
            answer += int(str(storey)[i])
            storey -= (int(str(storey)[i]) * unit)
        elif '6' <= str(storey)[i] <= '9' :
            answer += (10 - int(str(storey)[i]))
            storey += ((10 - int(str(storey)[i])) * unit)
        else :         
            if '0' <= str(storey)[i-1] <= '4' :
                answer += 5
                storey -= (5 * unit)
            else :
                answer += 5
                storey += (5 * unit)
        
        if origin_length != len(str(storey)) :
            origin_length = len(str(storey))
            i += 1
        else :
            unit *= 10
            i -= 1
    
    if '0' <= str(storey)[0] <= '5' :
        tmp = int(str(storey)[0])
        storey -= (tmp * unit)
        answer += tmp
    else :
        tmp = (10 - int(str(storey)[0]))
        storey += (tmp * unit)
        answer += (tmp+1)


    return answer




storey = 2455
print(solution(storey))