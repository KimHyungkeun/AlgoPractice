import sys

n, k = map(int, sys.stdin.readline().split())

cnt = 0
coins = []
for _ in range(n) :
    money = int(sys.stdin.readline().rstrip())
    coins.append(money)

coins.sort()

while coins and k != 0 :
    coin = coins.pop()
    if coin > k :
        continue

    val = (k // coin)
    cnt += val
    k %= coin

print(cnt)