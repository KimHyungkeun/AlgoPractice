import sys 

#올바른 방문 조건 1 : 한번씩만 방문
#올바른 방문 조건 2 : 나이트의 올바른 전진 방법 지킴 (1,2 or 2,1)
#올바른 방문 조건 3 : 마지막 방문 위치에서 최초 방문 위치로 조건2를 만족하여 갈수있어야 함

isvalid = True
visited = []
for i in range(36) :
    pos = sys.stdin.readline().rstrip()
    visited.append(pos)

if len(set(visited)) != 36 :
    isvalid = False

else :
    for i in range(1, 36) :
        
        if i == 35 :
            if abs(ord(visited[i][0]) - ord(visited[0][0])) == 1 and abs(ord(visited[i][1]) - ord(visited[0][1])) == 2 :
                break
            if abs(ord(visited[i][0]) - ord(visited[0][0])) == 2 and abs(ord(visited[i][1]) - ord(visited[0][1])) == 1 :
                break
            
            isvalid = False
            break

        if abs(ord(visited[i][0]) - ord(visited[i-1][0])) == 1 and abs(ord(visited[i][1]) - ord(visited[i-1][1])) == 2 :
            continue

        if abs(ord(visited[i][0]) - ord(visited[i-1][0])) == 2 and abs(ord(visited[i][1]) - ord(visited[i-1][1])) == 1 :
            continue

        isvalid = False
        break
   
        
if isvalid :
    print("Valid")
else :
    print("Invalid")