import sys

vowel = ['a', 'e', 'i', 'o', 'u']
while True :
    flag = True
    word = sys.stdin.readline().rstrip()
    if word == 'end' :
        break

    # 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    cnt = 0
    for v in vowel :
        if v in word :
            cnt = 1
            break
    
    if cnt == 0 :
        print("<" + word + ">" + " " + "is not acceptable.")
        continue

    # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    for i in range(len(word)-2) :
        if word[i] in vowel and word[i+1] in vowel and word[i+2] in vowel :
            flag = False
            break
        if word[i] not in vowel and word[i+1] not in vowel and word[i+2] not in vowel :
            flag = False
            break
    
    if not flag :
        print("<" + word + ">" + " " + "is not acceptable.")
        continue

    # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            if word[i] == 'e' or word[i] == 'o' :
                continue
            else :
                flag = False
                break
    
    if not flag :
        print("<" + word + ">" + " " + "is not acceptable.")
        continue

    print("<" + word + ">" + " " + "is acceptable.")