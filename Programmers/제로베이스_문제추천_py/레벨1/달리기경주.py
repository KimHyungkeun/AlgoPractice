def solution(players, callings):
    answer = []
    rank_dict = {}
    for i in range(len(players)) :
        rank_dict[players[i]] = i
        
    for c in callings :
        rank = rank_dict[c]
        rank_dict[c] -= 1
        rank_dict[players[rank-1]] += 1
        players[rank], players[rank-1] = players[rank-1], players[rank]
    
    for p in players :
        answer.append(p)
        
    return answer