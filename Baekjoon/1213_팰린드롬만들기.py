import sys

string = sys.stdin.readline().rstrip()
string = list(string)
string.sort()
alpha_dict = {}

for s in string :
    if s in alpha_dict :
        alpha_dict[s] += 1
    else :
        alpha_dict[s] = 1

mod_is_one_cnt = 0
mod_is_one = []
for key in alpha_dict.keys() :
    if alpha_dict[key] % 2 == 1 :
        mod_is_one_cnt += 1
        mod_is_one.append(key)

# 알파벳 등장 빈도수별로 2로 나눈 나머지연산을 진행한다
# 나머지연산 빈도수 결과에서, 나누어떨어지지 않는 알파벳들이 2개 이상 나타나면 팰린드롬이 아니다   
if mod_is_one_cnt >= 2 :
    print("I'm Sorry Hansoo")
else :
    ans = ""
    for key in alpha_dict.keys() :
        alpha_dict[key] //= 2
    reverse_dict = sorted(alpha_dict.items(), reverse=True, key = lambda x : x[0])
    
    for key in alpha_dict.keys() :
        for _ in range(alpha_dict[key]) :
            ans += key
    
    if mod_is_one :
        ans += mod_is_one[0]
    
    for r in reverse_dict :
        for _ in range(r[1]) :
            ans += r[0]
    
    print(ans)



