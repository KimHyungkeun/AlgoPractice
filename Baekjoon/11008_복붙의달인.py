import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n) :
    word, buffer = sys.stdin.readline().split()
    word = word.replace(buffer, '0')
    print(len(word))