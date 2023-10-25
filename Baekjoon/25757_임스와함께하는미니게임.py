import sys

n, types = sys.stdin.readline().split()
n = int(n)
player_list = []
for _ in range(n) :
    player_list.append(sys.stdin.readline().rstrip())

player_list = list(set(player_list))

# 윷놀이 : 1명 더 필요 (총 2명 가능)
if types == 'Y' :
    print(len(player_list))

# 같은 그림 찾기 : 2명 더 필요 (총 3명 가능)
if types == 'F' :
    print(len(player_list) // 2)

# 원카드 : 3명 더 필요 (총 4명 가능)
if types == 'O' :
    print(len(player_list) // 3)