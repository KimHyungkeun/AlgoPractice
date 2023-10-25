import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n) :
    word_list = list(sys.stdin.readline().rstrip())
    len_word_list_square = int(len(word_list) ** 0.5)
    
    # 초기 단어리스트들
    board = []
    tmp = []
    for w in word_list :
        tmp.append(w)
        if len(tmp) == len_word_list_square :
            board.append(tmp)
            tmp = []
    
    # 단어리스트를 왼쪽으로 90도 회전
    # 가장 오른쪽 열부터 시작하여, 해당 열을 행으로 만든다
    new_word_list = []
    for i in range(len_word_list_square-1, -1 , -1) :
        tmp = []
        for j in range(len_word_list_square) :
            tmp.append(board[j][i])
        new_word_list.append(tmp)
    
    new_word = ""
    for w in new_word_list :
        new_word += ''.join(w)
    
    print(new_word)
    