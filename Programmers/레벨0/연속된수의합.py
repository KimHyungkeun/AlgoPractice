def solution(num, total):
    answer = []

    start = -50

    tmp = []
    while True:
        for t in range(start, start+num):
            tmp.append(t)
        if sum(tmp) == total:
            break
        else:
            start += 1
            tmp = []

    answer = tmp
    return answer
