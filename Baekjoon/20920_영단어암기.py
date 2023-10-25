import sys

n, m = map(int,sys.stdin.readline().split())
word_dict = {}

for _ in range(n) :
    word = sys.stdin.readline().rstrip()
    if len(word) >= m :
        if word not in word_dict :
            word_dict[word] = 1
        else :
            word_dict[word] += 1
    
# 1. 알파벳 사전순으로 정렬
word_dict = sorted(word_dict.items(), key=lambda x : x[0])

# 2. 해당 단어의 길이가 길수록 앞쪽에 배치
word_dict = sorted(word_dict, key=lambda x : len(x[0]), reverse=True)

# 3. 자주 나오는 단어일수록 앞에 배치
word_dict = sorted(word_dict, key=lambda x : x[1], reverse=True)

for w in word_dict :
    print(w[0])
