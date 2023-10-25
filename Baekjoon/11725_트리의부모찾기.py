import sys
sys.setrecursionlimit(200000)

graph = {}
n = int(sys.stdin.readline().rstrip())

visited = [[False, 0] for _ in range(n+1)]
for i in range(1, n+1) :
    graph[i] = []

for _ in range(n-1) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs (graph, visited, start, parent) :
    if visited[start][0] :
        return
    visited[start][0] = True
    visited[start][1] = parent
    for g in graph[start] :
        dfs(graph, visited, g, start)

dfs(graph, visited, 1, 0)

for i in range(2, n+1) :
    print(visited[i][1])


