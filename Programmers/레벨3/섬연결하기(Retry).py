from collections import deque
def solution(n, costs):
    cnt = 0
    
    visited = [False] * n
    bridge_dict = {i:deque([]) for i in range(n)}
    
    for c in costs :
        bridge_dict[c[0]].append((c[1], c[2]))
        bridge_dict[c[1]].append((c[0], c[2]))
    
    for key,val in bridge_dict.items() :
        bridge_dict[key] = list(val)
        bridge_dict[key].sort(key = lambda x : x[1])
        bridge_dict[key] = deque(bridge_dict[key])
    
    def dfs(visited, bridge_dict, i, val) :
        nonlocal cnt
        if visited[i] :
            return
        if not bridge_dict[i] :
            return
        if visited.count(True) == n :
            return
        visited[i] = True
        cnt += val
        
        for dest in bridge_dict[i] :
            if bridge_dict[dest[0]] :
                i, val = bridge_dict[dest[0]].popleft()
                dfs(visited, bridge_dict, i, val)
    
    for idx in range(n) :
        if bridge_dict[idx] and visited.count(True) != n :
            i, val = bridge_dict[idx].popleft()
            dfs(visited, bridge_dict, i, val)
    
    return cnt

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
solution(n, costs)