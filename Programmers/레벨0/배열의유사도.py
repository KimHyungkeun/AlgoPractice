def solution(s1, s2):
    result = list(set(s1) & set(s2))
    answer = len(result)
    return answer