def solution(s):
    answer = []
    word_dict = {}
    
    for i in range(len(s)) :
        if s[i] not in word_dict :
            word_dict[s[i]] = [i]
            answer.append(-1)
        else :
            answer.append(i - word_dict[s[i]][-1])
            word_dict[s[i]].append(i)
    return answer