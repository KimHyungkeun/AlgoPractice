import sys

k = int(sys.stdin.readline())

for i in range(k) :
    arr = list(map(int, sys.stdin.readline().split()))
    total = arr[0]
    score_list = arr[1:]
    score_list.sort(reverse=True)

    score_gap = []
    for j in range(len(score_list)-1) :
        score_gap.append(score_list[j] - score_list[j+1])
    score_gap.sort(reverse=True)

    print("Class " + str(i+1))
    print("Max " + str(score_list[0]) + ", " + "Min " + str(score_list[-1]) + ", " + "Largest gap " + str(score_gap[0]))

