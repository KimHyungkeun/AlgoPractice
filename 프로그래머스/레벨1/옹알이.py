def solution(babbling):
    answer = 0
    babble_type = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        tmp = ""
        stack = []
        for i in b:
            tmp += i
            if tmp in babble_type:
                if not stack:
                    stack.append(tmp)
                    tmp = ""
                else:
                    if stack[-1] == tmp:
                        break
                    else:
                        stack.append(tmp)
                        tmp = ""
        if not tmp:
            answer += 1
    return answer


babbling = ["yeye"]
solution(babbling)
