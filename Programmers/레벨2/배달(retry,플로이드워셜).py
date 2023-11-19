# 정답참조 : 
# https://chanmuzi.tistory.com/185 (플로이드 워셜 알고리즘 사용)
# https://velog.io/@minji0801/%EC%98%A4%EB%8B%B5%EB%85%B8%ED%8A%B8%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%B0%EB%8B%AC-%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C
def solution(N, road, K) :
    # 음식 배달 최대시간이 500000시간이므로 맥시멈 값을 500001로 진행
    graph = [[500001 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1) :
        graph[i][i] = 0
    
    # for g in graph :
    #     print(g)

    for a,b,k in road :
        graph[a][b] = min(graph[a][b],k)
        graph[b][a] = min(graph[b][a],k)
    
    for g in graph :
        print(g)

    # k: 반드시 거쳐 지나가는 노드, i: 출발 노드, j: 도착 노드
    for k in range(1, N+1) :
        for i in range(1, N+1) :
            for j in range (1, N+1) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) 
                
    
    answers = [x for x in graph[1] if x <= K]
    return len(answers)
    

# 230919 78.1 / 100 : 시간초과
# def solution(N, road, K):
#     graph = {}
#     result = []
#     visited = []
#     total = 0
#     for i in range(1, N+1) :
#         graph[i] = []
#     for r in road :
#         graph[r[0]].append((r[1], r[2]))
#         graph[r[1]].append((r[0], r[2]))

#     def dfs(start, graph, result, total) :
#         if total > K :
#             return
#         if total <= K and start not in result :
#             result.append(start)
#         for g in graph[start] :
#             dfs(g[0], graph, result, total + g[1])
            
#     dfs(1, graph, result, total)
    
#     answer = len(result)
#     return answer

# N = 6
# road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# K = 4
N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
solution(N, road, K)