import sys

# 아빠새 몸통색, 꼬리색 / 엄마새 몸통색 꼬리색 순서로 입력
dad = list(sys.stdin.readline().split()) 
mom = list(sys.stdin.readline().split())
color_list = [dad[0], dad[1], mom[0], mom[1]]
color_permutaion = []

# 색깔조합을 진행
for i in range(len(color_list)) :
    for j in range(len(color_list)) :
        color_permutaion.append((color_list[i], color_list[j]))

# 몸통색이 다르면 몸통 색의 사전순으로, 몸통 색이 같다면 꼬리 색의 사전순으로 출력
color_permutaion = list(set(color_permutaion))
color_permutaion.sort(key = lambda x : x[1])
color_permutaion.sort(key = lambda x : x[0])

for c in color_permutaion :
    print(c[0], c[1])


