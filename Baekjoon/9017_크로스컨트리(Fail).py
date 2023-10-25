import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n) :
    total = int(sys.stdin.readline().rstrip())
    enter_list = list(map(int, sys.stdin.readline().split()))
    team_sets = sorted(list(set(enter_list)))
    team_dict = {}

    exception_team_list = []
    candidate_team_list = []
    visited = []

    # 팀 종류를 먼저 파악하고, 그 중 6명 미만인 팀들은 예외리스트에 넣는다
    for t in team_sets :
        if enter_list.count(t) < 6 :
            exception_team_list.append(t)
        else :
            team_dict[t] = []
    
    # 각 팀별 얻은 점수를 파악한다. 예외 리스트에 있는 팀은 0점 처리
    score = 0
    for i in range(len(enter_list)) :
        if enter_list[i] not in exception_team_list :
            score += 1
            visited.append(i)
            team_dict[enter_list[i]].append(score)
    
    max_score_list = max(team_dict.values(), key = lambda x : sum(x[:4]))
    max_score = sum(max_score_list[:4])

    for key in team_dict.keys() :
        if sum(team_dict[key][:4]) == max_score :
            candidate_team_list.append(key)

    # 동점자가 1팀이라면 해당 팀이 우승
    if len(candidate_team_list) == 1 :
        print(candidate_team_list[0])
    
    # 동점자가 여러명이라면, 각 팀의 5번째 선수 중에서 가장 점수가 낮은 인원팀을 보유한 팀이 이김 
    if len(candidate_team_list) > 1 :
        min_score_list = []
        for c in candidate_team_list :
            min_score_list.append((c, team_dict[c][4]))
        min_score_team = min(min_score_list, key = lambda x : x[1])
        print(min_score_team[0])
    
    
