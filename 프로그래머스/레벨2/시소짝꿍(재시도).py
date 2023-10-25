# 230321 오답
def solution(weights):
    answer = 0
    memory = []
    
    for i in range(len(weights)-1) :
        for j in range(i+1, len(weights)) :
            if [weights[i], weights[j]] in memory or [weights[j], weights[i]] in memory :
                continue
            sets1 = [weights[i]*2, weights[i]*3, weights[i]*4]
            sets2 = [weights[j]*2, weights[j]*3, weights[j]*4]
            result = set(sets1) & set(sets2)
            if result :
                answer += 1
            memory.append([weights[i], weights[j]])
    # print(memory)
    return answer

# 답봤음 https://yejin72.tistory.com/109
from collections import defaultdict
def solution(weights):
    answer = 0
    
    info = defaultdict(int)
    weights.sort()
    for w in weights :
        answer += info[w] + info[(w/2)] + info[w*2] + info[(w*2)/3] + info[(w*3)/2] + info[(w*3)/4] + info[(w*4)/3]
        info[w] += 1
    
 
    return answer