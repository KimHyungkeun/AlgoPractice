def solution(n):
    result = []

    arr = []
    total = 0
    for i in range(n) :
        total += (i+1)
    for _ in range(n) :
        arr.append([0]*n)
    
    num = 1
    i,j = 0,0
    while num <= total :
        while i < n and arr[i][j] == 0:
            arr[i][j] = num
            i += 1
            num += 1
        
        i -= 1
        j += 1
        while j < n and arr[i][j] == 0 :
            arr[i][j] = num
            j += 1
            num += 1
        
        i -= 1
        j -= 2
        while i > 0 and j > 0 and arr[i][j] == 0 :
            arr[i][j] = num
            i -= 1
            j -= 1
            num += 1

        i += 2
        j += 1
       
    for a in arr :
        for r in a :
            if r == 0 :
                break
            result.append(r)
    
    return result

n = 5
solution(n)