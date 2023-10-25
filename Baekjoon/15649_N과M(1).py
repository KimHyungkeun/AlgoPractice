import sys

n, m = map(int, sys.stdin.readline().split())

def recursion(start, arr, graph) :
    if len(arr) == m :
        for a in arr :
            print(a, end=' ')
        print()
        return
    for i in graph[start] :
        if i not in arr :
            arr.append(i)
            recursion(i, arr, graph)
            arr.pop()

graph = {}
for i in range(1, n+1) :
    graph[i] = [j for j in range(1, n+1) if i != j]

for i in range(1, n+1) :
    arr = [i]
    recursion(i, arr, graph)
