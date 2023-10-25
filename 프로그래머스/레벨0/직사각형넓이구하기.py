def solution(dots):
    answer = 0
    type_x = []
    type_y = []

    for d in dots:
        if d[0] not in type_x:
            type_x.append(d[0])
        if d[1] not in type_y:
            type_y.append(d[1])

    answer = abs(type_x[0]-type_x[1]) * abs(type_y[0]-type_y[1])
    return answer
