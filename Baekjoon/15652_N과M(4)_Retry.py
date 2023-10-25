# 231023 정답코드 참고
# https://ji-gwang.tistory.com/255
import sys

n, m = map(int, sys.stdin.readline().split())
out = []

def solve (depth, idx, n, m) :
    if depth == m :
        print(' '.join(out))
        return
    for i in range(idx, n + 1) :
        out.append(str(i))
        solve(depth + 1, i, n, m)
        out.pop()

solve(0, 1, n, m)

# 231023 7%에서 시간초과
# def recursion(start, arr, graph) :
#     if len(arr) == m :
#         sort_arr = sorted(arr)
#         if sort_arr not in visited :
#             visited.append(sort_arr)
#             for a in arr :
#                 print(a, end=' ')
#             print()
#         return
#     for i in graph[start] :
#         arr.append(i)
#         recursion(i, arr, graph)
#         arr.pop()

# graph = {}
# for i in range(1, n+1) :
#     graph[i] = [j for j in range(1, n+1)]

# visited = []
# for i in range(1, n+1) :
#     arr = [i]
#     recursion(i, arr, graph)
