import sys

king, queen, rook, bishop, knight, pawn = map(int, sys.stdin.readline().split(" "))

print(1 - king, 1 - queen, 2 - rook, 2 - bishop, 2 - knight, 8 - pawn)

