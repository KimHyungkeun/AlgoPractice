def solution(players, callings):
    result = []
    player_with_order = {}
    for i in range(len(players)) :
        player_with_order[players[i]] = i
    
    for c in callings :
        rank = player_with_order[c]
        before_player = players[rank-1]
        players[rank-1], players[rank] = players[rank], players[rank-1]
        player_with_order[c] -= 1
        player_with_order[before_player] += 1
        
    
    dictionary = sorted(player_with_order.items())
    dictionary.sort(key = lambda x : x[1])
    
    for d in dictionary :
        result.append(d[0])
    
    return result