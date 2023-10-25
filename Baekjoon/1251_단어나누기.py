# 230518 재풀이
import sys
word = sys.stdin.readline().rstrip()

word_list = []
for i in range(1, len(word)-1) :
    for j in range(i+1, len(word)) :
        first = list(word[:i])
        middle = list(word[i:j])
        last = list(word[j:])

        first.reverse()
        middle.reverse()
        last.reverse()

        word_list.append(''.join(first) + ''.join(middle) +''.join(last))

word_list = list(set(word_list))
word_list.sort()
print(word_list[0])




# 230424 답봤음
# 참고 : https://data-bank.tistory.com/38
# import sys

# word = list(sys.stdin.readline().rstrip())
# word_list = set({})

# for i in range(1, len(word)-1) :
#     for j in range(i+1, len(word)) :
#         word1 = word[:i]
#         word2 = word[i:j]
#         word3 = word[j:]

#         word1.reverse()
#         word2.reverse()
#         word3.reverse()

#         word_list.add(''.join(word1)+''.join(word2)+''.join(word3))

# word_list = list(word_list)
# word_list.sort()
# print(word_list[0])

# 230423 오답. 채점 7%에서 틀림
# import sys

# word = list(sys.stdin.readline().rstrip())
# word_list = set({})

# last_len = len(word)
# first_slash = last_len - 2
# second_slash = last_len - 1

# while True : 
#     word_partition1 = word[:first_slash]
#     word_partition2 = word[first_slash:second_slash]
#     word_partition3 = word[second_slash:]

#     result = ''
#     word_partition1.reverse()
#     word_partition2.reverse()
#     word_partition3.reverse()

#     result += ''.join(word_partition1)
#     result += ''.join(word_partition2)
#     result += ''.join(word_partition3)

#     word_list.add(result)
    
#     if first_slash == 1 :
#         break
    
#     first_slash -= 1

#     # print(first_slash)

# while True : 
#     word_partition1 = word[:first_slash]
#     word_partition2 = word[first_slash:second_slash]
#     word_partition3 = word[second_slash:]

#     result = ''
#     word_partition1.reverse()
#     word_partition2.reverse()
#     word_partition3.reverse()

#     result += ''.join(word_partition1)
#     result += ''.join(word_partition2)
#     result += ''.join(word_partition3)

#     word_list.add(result)
    
#     if second_slash == 2 :
#         break
    
#     second_slash -= 1
 
#     # print(second_slash)


# word_list = list(word_list)
# word_list.sort()
# print(min(word_list))
