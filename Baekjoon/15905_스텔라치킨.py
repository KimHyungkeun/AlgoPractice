import sys

n = int(sys.stdin.readline().rstrip())

if n == 5 :
    print(0)

else :
    cnt = 0
    rank_list = []
    for _ in range(n) :
        rank, penalty = map(int, sys.stdin.readline().split())
        rank_list.append((rank, penalty))

    rank_list.sort(key = lambda x : x[1])
    rank_list.sort(key = lambda x : x[0], reverse=True)

    for i in range(5, len(rank_list)) :
        if rank_list[4][0] == rank_list[i][0] and rank_list[4][1] < rank_list[i][1]:
            cnt += 1
        else :
            break
    
    print(cnt)
