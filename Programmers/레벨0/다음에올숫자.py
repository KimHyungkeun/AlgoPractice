def solution(common):
    answer = 0

    is_plus = False
    plus_list = []
    multi_list = []

    for i in range(len(common)-1, 0, -1):
        if not plus_list:
            plus_list.append(common[i] - common[i-1])
        else:
            if plus_list[-1] == common[i] - common[i-1]:
                is_plus = True
            else:
                multi_list.append(common[i] // common[i-1])

    if is_plus:
        answer = common[-1] + plus_list[-1]
    else:
        answer = common[-1] * multi_list[-1]

    return answer
