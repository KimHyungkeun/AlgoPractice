def solution(X, Y):
    answer = ''
    X_dict = {}
    Y_dict = {}

    for n in X:
        if n not in X_dict:
            X_dict[n] = 1
        else:
            X_dict[n] += 1

    for n in Y:
        if n not in Y_dict:
            Y_dict[n] = 1
        else:
            Y_dict[n] += 1

    for key in X_dict.keys():
        if key in Y_dict:
            for _ in range(min(X_dict[key], Y_dict[key])):
                answer += key

    if not answer:
        return "-1"

    answer = list(answer)
    answer.sort(reverse=True)
    answer = ''.join(answer)

    if len(set(list(answer))) == 1 and answer[0] == '0':
        answer = "0"
    return answer
