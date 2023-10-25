def solution(keymap, targets):
    answer = []
    for i in range(len(targets)) :
        cnt = 0
        for j in range(len(targets[i])) :
            idx_arr = []
            # i번째 target의 j번째 글자에 대해서, 
            # 각 keymap 별로 최소로 닿을 수 있는 클릭 횟수를 각각 구하고 그 중 최솟값을 구함 
            for k in range(len(keymap)) :
                for l in range(len(keymap[k])) :
                    if keymap[k][l] == targets[i][j] :
                        idx_arr.append(l+1)
                        break
            if not idx_arr :
                cnt = -1
                break

            cnt += min(idx_arr)

        answer.append(cnt)
    return answer

# keymap = ["ABACD", "BCEFD"]
# targets = ["ABCD","AABB"]
# keymap = ["AA"]
# targets = ["B"]
keymap = ["AGZ", "BSSS"]
targets = ["ASA","BGZ"]
solution(keymap, targets)