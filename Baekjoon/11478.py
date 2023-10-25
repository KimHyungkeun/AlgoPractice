import sys

word = sys.stdin.readline().rstrip()
sets = set([])

for i in range(1, len(word)+1) :
    for j in range(len(word)) :
        sets.add(''.join(word[j:j+i]))
print(len(sets))