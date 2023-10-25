import sys

t = int(sys.stdin.readline().rstrip())

def recursion(word, left, right) :
    global cnt
    if left >= right :
        return 1
    elif word[left] != word[right] :
        return 0
    else :
        cnt += 1
        return recursion(word, left+1, right-1)

def isPalindrom(word) :
    global cnt
    cnt += 1
    return recursion(word, 0, len(word)-1)

for _ in range(t) :
    cnt = 0
    word = sys.stdin.readline().rstrip()
    result = isPalindrom(word)
    print(result, cnt)