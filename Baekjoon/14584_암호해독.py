import sys

encrypted_word = list(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline().rstrip())

candidate_wordlist = []
for _ in range(n) :
    candidate_wordlist.append(sys.stdin.readline().rstrip())

candidate_list = []
decrypt_candidate = []
for i in range(25) :
    tmp = []
    for j in range(len(encrypted_word)) :
        plus = ord(encrypted_word[j]) + i
        if plus > 122 :
            plus -= 26
        tmp.append(chr(plus))
    
    decrypt_candidate.append(''.join(tmp))

for c in candidate_wordlist :
    for d in decrypt_candidate :
        if c in d :
            candidate_list.append(d)
            break
    if candidate_list :
        break

print(candidate_list[0])




    

