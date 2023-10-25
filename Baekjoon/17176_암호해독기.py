import sys

keyword = {0 : ' '}

start = 65
for i in range(1, 27) :
    keyword[i] = chr(start)
    start += 1

start = 97
for i in range(27, 53) :
    keyword[i] = chr(start)
    start += 1

n = int(sys.stdin.readline())
password = list(map(int, sys.stdin.readline().split()))
decrypted = list(sys.stdin.readline().rstrip())

for i in range(len(password)) :
    password[i] = keyword[password[i]]

password.sort()
decrypted.sort()

if ''.join(password) == ''.join(decrypted) :
    print("y")
else :
    print("n")
