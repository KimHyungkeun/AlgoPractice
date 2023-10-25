# 230927 Retry Success
import sys
sys.setrecursionlimit(200000)

n, m, r = map(int, sys.stdin.readline().split())

graph = {}
visited = [[False, 0] for _ in range(n+1)]

for i in range(1, n+1) :
    graph[i] = []

for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for key in graph.keys() :
    graph[key].sort()

def dfs (graph, visited, start) :
    global cnt
    if visited[start][0] :
        return
    cnt += 1
    visited[start][0] = True
    visited[start][1] = cnt
    for g in graph[start] :
        dfs(graph, visited, g)

cnt = 0
dfs(graph, visited, r) 

for i in range (1, n+1) :
    print(visited[i][1])

# 230925 추후 재시도
# import sys
# sys.setrecursionlimit(200000)

# graph = {}
# n, m, r = map(int, sys.stdin.readline().split())
# for i in range(1, n+1) :
#     graph[i] = []

# visited = []
# for _ in range(n+1) :
#     visited.append([False, 0])
# cnt = 0

# for _ in range(m) :
#     start, end = map(int, sys.stdin.readline().split())
#     graph[start].append(end)
#     graph[end].append(start)

# for key in graph.keys() :
#     graph[key].sort()

# def dfs (graph, visited, start) : 
#     global cnt
#     if visited[start][0] :
#         return
#     cnt += 1
#     visited[start][0] = True
#     visited[start][1] = cnt
#     for g in graph[start] :
#         dfs(graph, visited, g)

# dfs(graph, visited, r)


# for i in range(1, n+1) :
#     print(visited[i][1])

