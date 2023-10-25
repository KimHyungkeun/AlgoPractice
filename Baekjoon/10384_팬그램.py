import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1,n+1) :
    alpha_dict = {chr(i):0 for i in range(97,123)}
    sentence = list(sys.stdin.readline().rstrip())

    for s in sentence :
        if 'a' <= s <= 'z' :
            alpha_dict[s] += 1
        if 'A' <= s <= 'Z' :
            alpha_dict[chr(ord(s)+32)] += 1

    # 각 알파벳별 빈도수 딕셔너리 내의 value들을 비교하여
    # 그중 최솟값이 곧 알파벳별 최소 빈도수가 된다  
    frequency = set(alpha_dict.values())

    if min(frequency) == 0 :
        print("Case " + str(i) + ": " + "Not a pangram")
    if min(frequency) == 1 :
        print("Case " + str(i) + ": " + "Pangram!")
    if min(frequency) == 2 :
        print("Case " + str(i) + ": " + "Double pangram!!")
    if min(frequency) >= 3 :
        print("Case " + str(i) + ": " + "Triple pangram!!!")