# 231019 재시도
import sys

def recursion(n) :
    if n == 1 :
        return ['*']
    
    stars = recursion(n // 3)
    l = []

    for s in stars :
        l.append(s*3)
    for s in stars :
        l.append(s + ' '*(n // 3) + s)
    for s in stars :
        l.append(s*3)
    
    return l


n = int(sys.stdin.readline().rstrip())
print('\n'.join(recursion(n)))

# 231016 답봤음
# import sys

# def recursion(len) :
#     if len == 1 :
#         return ['*']
    
#     stars = recursion(len // 3)
#     l = []

#     for s in stars :
#         l.append(s*3)
#     for s in stars :
#         l.append(s+' '*(len//3)+s)
#     for s in stars :
#         l.append(s*3)
    
#     print(l)
#     return l


# n = int(sys.stdin.readline().rstrip())
# print('\n'.join(recursion(n)))
