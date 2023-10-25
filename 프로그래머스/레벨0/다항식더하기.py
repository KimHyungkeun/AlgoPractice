def solution(polynomial):
    answer = ''
    contain_x = 0
    only_number = 0

    polynomial = polynomial.split(" + ")

    for p in polynomial:
        if "x" in p:
            if p == "x":
                contain_x += 1
            else:
                contain_x += int(p.split("x")[0])
        else:
            only_number += int(p)

    if contain_x == 0:
        answer += str(only_number)
    else:
        if only_number == 0:
            if contain_x == 1:
                answer += 'x'
            else:
                answer += str(contain_x) + 'x'
        else:
            if contain_x == 1:
                answer += 'x' + ' + ' + str(only_number)
            else:
                answer += str(contain_x) + 'x' + ' + ' + str(only_number)

    return answer


polynomial = "x"
print(solution(polynomial))
