import sys

n, k = map(int, sys.stdin.readline().split())
country_dict = {}

for _ in range(n) :
    nums = list(map(int, sys.stdin.readline().split()))
    country_dict[nums[0]] = nums[1:]

# 동메달 기준으로 등수 결정
country_dict = sorted(country_dict.items(), key=lambda x : x[1][2], reverse=True)

# 은메달 기준으로 등수 결정
country_dict = sorted(country_dict, key=lambda x : x[1][1], reverse=True)

# 금메달 기준으로 등수 결정
country_dict = sorted(country_dict, key=lambda x : x[1][0], reverse=True)

rank = 1
equal_rank = 0

for i in range(1, len(country_dict)) :
    if country_dict[i-1][1] == country_dict[i][1] :
        equal_rank += 1
    else :
        rank += equal_rank
        equal_rank = 0
    
    if country_dict[i][0] == k :
        break

print(rank+1)