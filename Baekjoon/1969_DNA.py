import sys

n, m = map(int, sys.stdin.readline().split())

hamming_distance = ""
dna_list = []
for _ in range(n) :
    dna = sys.stdin.readline().rstrip()
    dna_list.append(dna)

# 1. hamming_distance 합이 가장 작은 dna 만들기
for i in range(m) :
    spell_freqency = {}
    for j in range(n) :
        if dna_list[j][i] not in spell_freqency :
            spell_freqency[dna_list[j][i]] = 1
        else :
            spell_freqency[dna_list[j][i]] += 1
    
    # 알파벳 순서대로 먼저 정렬, 그 후 가장 많은 등장빈도수를 가지는 알파벳 순으로 정렬
    sort_by_alpha_dict = sorted(spell_freqency.items(), key=lambda x : x[0])
    sort_by_val = sorted(sort_by_alpha_dict, key=lambda x : x[1], reverse=True)
    hamming_distance += sort_by_val[0][0]

# 2. hamming_distance 합
result = 0
for i in range(n) :
    cnt = 0
    for j in range(m) :
        if dna_list[i][j] != hamming_distance[j] :
            cnt += 1
    result += cnt

print(hamming_distance)
print(result)