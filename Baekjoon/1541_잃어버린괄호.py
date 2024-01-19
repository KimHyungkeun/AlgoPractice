import sys

sentence = sys.stdin.readline().rstrip()

# 1. "-"를 기준으로 split
split_from_minus = sentence.split("-")

# 2. 수식 중 "+"가 들어간 수식이있다면, 해당 수식을 계산한 결과값으로 수정
for i in range(len(split_from_minus)) :
    if '+' in split_from_minus[i] :
        total = 0
        split_from_plus = split_from_minus[i].split("+")
        for val in split_from_plus :
            total += int(val)
        split_from_minus[i] = total
    else :
        split_from_minus[i] = int(split_from_minus[i])

# 3. 2.를 완료한 수식에 대해 다시 마이너스 시킴
if len(split_from_minus) == 1 :
    result = split_from_minus[0]
else :
    result = split_from_minus[0]
    for i in range(1, len(split_from_minus)) :
        result -= split_from_minus[i]

print(result)
