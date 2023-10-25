# 230930 Retry Success
import sys

keyboard = {
    'q' : (0,0,True), 'w' : (0,1,True), 'e' : (0,2,True), 'r' : (0,3,True), 't' : (0,4,True), 'y' : (0,5,False), 'u' : (0,6,False), 'i' : (0,7,False), 'o' : (0,8,False), 'p' : (0,9,False),
    'a' : (1,0,True), 's' : (1,1,True), 'd' : (1,2,True), 'f' : (1,3,True), 'g' : (1,4,True), 'h' : (1,5,False), 'j' : (1,6,False), 'k' : (1,7,False), 'l' : (1,8,False),
    'z' : (2,0,True), 'x' : (2,1,True), 'c' : (2,2,True), 'v' : (2,3,True), 'b' : (2,4,False), 'n' : (2,5,False), 'm' : (2,6,False)
}

l, r = sys.stdin.readline().split()
l_pos = [keyboard[l][0], keyboard[l][1]]
r_pos = [keyboard[r][0], keyboard[r][1]]

cnt = 0
word = list(sys.stdin.readline().rstrip())

for w in word :
    if keyboard[w][2] :
        cnt += abs(l_pos[0] - keyboard[w][0]) + abs(l_pos[1] - keyboard[w][1])
        cnt += 1
        l_pos = [keyboard[w][0], keyboard[w][1]]
    else :
        cnt += abs(r_pos[0] - keyboard[w][0]) + abs(r_pos[1] - keyboard[w][1])
        cnt += 1
        r_pos = [keyboard[w][0], keyboard[w][1]]

print(cnt)


# 첫째 시도: 4%에서 오답
# 질문게시판 봤음 : 한글자음쪽 자판은 왼쪽으로만, 한글모음쪽 자판은 오른쪽 손가락으로만 쳐야함

# 둘째 시도 : 4%에서 오답
# 'b'자판이 한글자음인줄 알았는데, 모음자판이었음 

# import sys

# keyboard = {'q':(0,0,True), 'w':(0,1,True), 'e':(0,2,True), 'r':(0,3,True), 't':(0,4,True), 'y':(0,5,False), 'u':(0,6,False), 'i':(0,7,False), 'o':(0,8,False), 'p':(0,9,False),
#             'a':(1,0,True), 's':(1,1,True), 'd':(1,2,True), 'f':(1,3,True), 'g':(1,4,True), 'h':(1,5,False), 'j':(1,6,False), 'k':(1,7,False), 'l':(1,8,False),
#             'z':(2,0,True), 'x':(2,1,True), 'c':(2,2,True), 'v':(2,3,True), 'b':(2,4,False), 'n':(2,5,False), 'm':(2,6,False)}


# left, right = sys.stdin.readline().split()
# left_pos = [keyboard[left][0], keyboard[left][1]]
# right_pos = [keyboard[right][0], keyboard[right][1]]
# word = sys.stdin.readline().rstrip()

# cnt = 0
# for w in word :
#     w_pos = keyboard[w]

#     if w_pos[2] :
#         left_to_w = abs(left_pos[0] - w_pos[0]) + abs(left_pos[1] - w_pos[1])
#         cnt += (left_to_w + 1)
#         left_pos = [w_pos[0], w_pos[1]]
#     else :
#         right_to_w = abs(right_pos[0] - w_pos[0]) + abs(right_pos[1] - w_pos[1])
#         cnt += (right_to_w + 1)
#         right_pos = [w_pos[0], w_pos[1]]

# print(cnt)