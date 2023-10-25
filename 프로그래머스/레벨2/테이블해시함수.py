def solution(data, col, row_begin, row_end):
    answer = 0

    # col번째 컬럼 값을 기준으로 오름차순 정렬
    data.sort(key = lambda x : x[col-1])
    
    new_arr = []
    tmp = []
    
    # 만약 동일한 col번째 연속으로 존재할 경우, 그 부분에 대해서는 기본키(첫번째컬럼) 기준으로 내림차순 정렬 할것 
    for d in data :
        if not tmp :
            tmp.append(d)
        else :
            if tmp[-1][col-1] == d[col-1] :
                tmp.append(d)
            else :
                tmp.sort(key = lambda x : x[0], reverse=True)
                new_arr.extend(tmp)
                tmp = []
                tmp.append(d)
    if tmp :
        new_arr.extend(tmp)
    data = new_arr
    
    result = []
    for idx in range(row_begin-1, row_end) :
        total = 0
        for a in data[idx] :
            total += (a % (idx+1))
        result.append(total)
    
    # row_begin번째부터 row_end까지 mod한 값들에 대해 XOR 연산
    answer = result[0]
    for i in range(1, len(result)) :
        answer ^= result[i]
    return answer