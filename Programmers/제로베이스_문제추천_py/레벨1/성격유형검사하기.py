def dict_sort(types) :
    
    types.sort(key = lambda x : x[0])
    types.sort(key = lambda x : x[1], reverse=True)
    
    return types

def solution(survey, choices):
    answer = ''
    type_dict = {'R':0, 'T':0 , 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    score_dict = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    
    for i in range(len(survey)) :
        if choices[i] >= 5 :
            type_dict[survey[i][1]] += score_dict[choices[i]]
        else :
            type_dict[survey[i][0]] += score_dict[choices[i]]
    
    result = list(type_dict.items())
    
    type1 = [result[0], result[1]]
    type1 = dict_sort(type1)
    
    type2 = [result[2], result[3]]
    type2 = dict_sort(type2)
    
    type3 = [result[4], result[5]]
    type3 = dict_sort(type3)
    
    type4 = [result[6], result[7]]
    type4 = dict_sort(type4)
    
    answer = type1[0][0] + type2[0][0] + type3[0][0] + type4[0][0]
    return answer