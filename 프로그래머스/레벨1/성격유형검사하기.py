def solution(survey, choices):
    answer = ''
    types = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0,'A':0, 'N':0}
    
    tmp_dict = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    for i in range(len(choices)) :
        if choices[i] <= 3 :
            types[survey[i][0]] += tmp_dict[choices[i]]
        if choices[i] >= 5 :
            types[survey[i][1]] += tmp_dict[choices[i]]

    types = list(types.items())

    for i in range(0, len(types), 2) :
        tmp_list = [types[i], types[i+1]]
        tmp_list.sort(key = lambda x : x[0])
        tmp_list.sort(key = lambda x : x[1], reverse=True)
        answer += tmp_list[0][0]
         
    print(answer)
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
solution(survey, choices)