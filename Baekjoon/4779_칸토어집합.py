import sys

def recursion (arr) :
    if len(arr) <= 1:
        return ''.join(arr)
    
    left_i = len(arr) // 3
    right_i = (len(arr) // 3) * 2

    left_result = recursion(arr[:left_i])
    for i in range(left_i, right_i) :
        arr[i] = ' '
    right_result = recursion(arr[right_i:])
    
    return left_result + ''.join(arr[left_i:right_i]) + right_result

while True :
    try :
        n = int(sys.stdin.readline().rstrip())
        arr = ['-'] * 3**n
        result = recursion(arr)
        print(result)
    except :
        break