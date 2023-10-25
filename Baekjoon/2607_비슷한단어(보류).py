import sys

n = int(sys.stdin.readline().rstrip())

origin = sys.stdin.readline().rstrip()
origin_keyword = {}
origin_sets = set([])
for o in origin :
    origin_sets.add(o)
    if o not in origin_keyword :
        origin_keyword[o] = 1
    else :
        origin_keyword[o] += 1

cnt = 0
for _ in range(n-1) :
    word_keyword = {}
    word_sets = set([])
    word = sys.stdin.readline().rstrip()

    for w in word :
        word_sets.add(w)
        if w not in word_keyword :
            word_keyword[w] = 1
        else :
            word_keyword[w] += 1






