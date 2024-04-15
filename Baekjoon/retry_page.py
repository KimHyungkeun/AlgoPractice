# cur_lat = 37.5544069
# cur_lnt = 126.8998666

# target_x = 37.552788
# target_y = 126.89939


cur_lat = 37.5544069
cur_lnt = 126.8998666

target_x = 37.55698
target_y = 126.89872

answer = (abs(cur_lat - target_x) ** 2 + abs(cur_lnt - target_y) ** 2) ** 0.5
print(answer)