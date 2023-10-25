def solution(k, tangerine):
    answer = 0
    orange_dict = {}
    
    # 오렌지 크기 종류별 갯수 딕셔너리 생성
    for t in tangerine :
        if t not in orange_dict :
            orange_dict[t] = 1
        else :
            orange_dict[t] += 1
    
    # 갯수 기준으로 딕셔너리 내림차순 정렬
    sorted_dict = sorted(orange_dict.items(), key = lambda x : x[1] ,reverse=True)
    
    # 귤을 하나씩 주워담고, total이 k갯수와 같으면 종료
    total = 0
    for s in sorted_dict :
        answer += 1
        for _ in range(s[1]) :
            total += 1
            if total == k :
                break
        if total == k :
            break
             
    return answer