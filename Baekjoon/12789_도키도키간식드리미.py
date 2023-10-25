import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
first_q = deque(list(map(int, sys.stdin.readline().split())))
standby_q = deque([])

is_nice = True
idx = 1
while idx <= n :

    # 임시 대기열에만 사람이 있고, 임시 대기열 앞 번호가 idx번째가 아니면 여기서 종료
    if (standby_q and not first_q) and standby_q[0] != idx :
        is_nice = False
        break

    # 첫 대기열에 사람이 있을 때, 첫 대기열 맨 앞사람이 idx번째이면
    # 바로 빠져 나가고 idx 순번이 증가
    if first_q :
        if first_q[0] == idx :
            first_q.popleft()
            idx += 1
            continue

    # 임시 대기열에 사람이 있을 때, 임시 대기열 맨 앞사람이 idx번째 이면
    # 바로 빠져 나가고 idx 순번이 증가
    if standby_q :
        if standby_q[0] == idx :
            standby_q.popleft()
            idx += 1
            continue
    
    # 만약 아무런 경우도 아니라면, 첫 대기열 사람은 임시 대기열로 이동
    if first_q :
        standby_q.appendleft(first_q.popleft())


if is_nice :
    print("Nice")
else :
    print("Sad")