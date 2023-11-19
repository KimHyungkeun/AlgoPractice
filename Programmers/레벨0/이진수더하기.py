def solution(bin1, bin2):
    answer = ''
    stack = []
    bin1 = list(reversed(list(bin1)))
    bin2 = list(reversed(list(bin2)))

    min_length = min(len(bin1), len(bin2))
    max_length = max(len(bin1), len(bin2))
    i = 0
    tmp = 0
    while i < min_length:
        tmp = int(bin1[i]) + int(bin2[i])
        if stack:
            tmp += stack.pop()
        if tmp >= 2:
            stack.append(1)
            answer += str(tmp - 2)
        else:
            answer += str(tmp)
        i += 1

    extra_bin = ""
    if len(bin1) > len(bin2):
        extra_bin = bin1
    else:
        extra_bin = bin2

    while i < max_length:
        if stack:
            tmp = int(extra_bin[i]) + stack.pop()
        else:
            tmp = int(extra_bin[i])

        if tmp >= 2:
            stack.append(1)
            answer += str(tmp - 2)
        else:
            answer += str(tmp)
        i += 1

    if stack:
        answer += str(stack.pop())

    answer = ''.join(reversed(list(answer)))
    return answer


bin1 = "1111"
bin2 = "1"
print(solution(bin1, bin2))
