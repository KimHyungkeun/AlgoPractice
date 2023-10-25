# 231001 Retry Success
import sys


def merge_sort(arr, p, r) : # A[p..r]을 오름차순 정렬한다.
    if p < r and cnt <= k: 
        q = (p + r) // 2 # q는 p, r의 중간 지점
        merge_sort(arr, p, q)    # 전반부 정렬
        merge_sort(arr, q + 1, r)  # 후반부 정렬
        merge(arr, p, q, r)        # 병합
    
def merge(arr, p, q, r) :
    global cnt, result
    i = p
    j = q + 1
    tmp = []
    while i <= q and j <= r :
        if arr[i] <= arr[j] :
            tmp.append(arr[i]) # tmp[t] <- A[i]; t++; i++;
            i += 1
        else : 
            tmp.append(arr[j]) # tmp[t] <- A[j]; t++; j++;
            j += 1
    
    while i <= q :  # 왼쪽 배열 부분이 남은 경우
        tmp.append(arr[i]) # tmp[t] <- A[i]; t++; i++;
        i += 1

    while j <= r :  # 오른쪽 배열 부분이 남은 경우
        tmp.append(arr[j]) # tmp[t] <- A[j]; t++; j++;
        j += 1
    
    i = p 
    t = 0
    while i <= r : # 결과를 A[p..r]에 저장
        arr[i] = tmp[t]
        cnt += 1
        if cnt == k :
            result = arr[i]
            break
        i += 1
        t += 1 
        
n, k = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
result = -1

merge_sort(arr, 0, n-1)
print(result)

# 230927 추후 재시도 진행
# import sys

# def merge(arr, p, q, r) :
#     global cnt, result
#     i = p
#     j = q+1
#     tmp = []

#     while i <= q and j <= r :
#         if arr[i] <= arr[j] :
#             tmp.append(arr[i])
#             i += 1
#         else :
#             tmp.append(arr[j])
#             j += 1
        
#     while i <= q :
#         tmp.append(arr[i])
#         i += 1
    
#     while j <= r :
#         tmp.append(arr[j])
#         j += 1
    
#     i = p
#     t = 0
#     while i <= r :
#         arr[i] = tmp[t]
#         cnt += 1
#         if cnt == k :
#             result = arr[i]
#             break
#         i += 1
#         t += 1
    

# def merge_sort(arr, p, r) :
#     if p < r and cnt <= k:
#         q = (p + r) // 2
#         merge_sort(arr, p, q) # 전반부 정렬
#         merge_sort(arr, q+1, r) # 후반부 정렬
#         merge(arr, p, q, r) # 병합

# n, k = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# cnt = 0
# result = -1
# merge_sort(arr, 0, n-1)
# print(result)