# 230907 Retry Success
import sys

n = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()

if len(string) <= 25 :
    print(string)

if len(string) > 25 :
    substr = string[11:-12]
    # 한 문장으로 끝나는 단어였다면, 마지막 "."을 제외하고는 또다른 "."가 나와선 안된다
    if "." in substr :
        print(string[:9] + "......" + string[-10:])
    else :
        print(string[:11] + "..." + string[-11:]) 

# 5%에서 틀린 답안
# import sys

# n = int(sys.stdin.readline().rstrip())
# sentence = sys.stdin.readline().rstrip()

# if n <= 25 :
#     print(sentence)
# else :
#     sub_word = sentence[11:-11]
#     if sub_word.count(".") == 1 and sub_word[-1] == ".":
#         print(sentence[:11] + "..." + sentence[-11:])
#     else :
#         print(sentence[:9] + "......" + sentence[-10:])

# 참고 답안
# import sys

# N = int(sys.stdin.readline().rstrip())
# S = sys.stdin.readline().rstrip()
# if N <= 25:
#     print(S)
# elif N > 25:
#     print(S[11:-12])
#     if "." in S[11:-12]:
#         print(S[:9] + "......" + S[-10:])
#     else:
#         print(S[:11] + "..." + S[-11:])