import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
graph = {}

for i in range(1, n+1) :
    graph[i] = []
visited = []
for i in range(n+1) :
    visited.append([False, 0])

for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for key in graph.keys() :
    graph[key].sort(reverse=True)


def bfs (graph, visited, start, cnt) :
    q = deque([start])

    while q :
        next = q.popleft()
        if visited[next][0] :
            continue
        cnt += 1
        visited[next][0] = True
        visited[next][1] = cnt

        for g in graph[next] :
            if not visited[g][0] :
                q.append(g)

cnt = 0
bfs(graph, visited, r, cnt)

for i in range(1, n+1) :
    print(visited[i][1])