import sys

n = int(sys.stdin.readline().rstrip())

before_dict = {}
after_dict = {}
vowel = ['a', 'e', 'i', 'o', 'u']

before = sys.stdin.readline().rstrip()
after = sys.stdin.readline().rstrip()

sort_before = sorted(before)
sort_after = sorted(after)

except_vowel_before = ""
except_vowel_after = ""

if sort_before == sort_after and (before[0] == after[0] and before[-1] == after[-1]):
    for b in before :
        if b not in vowel :
            except_vowel_before += b
    
    for a in after :
        if a not in vowel :
            except_vowel_after += a
    
    if except_vowel_before == except_vowel_after :
        print("YES")
    else :
        print("NO")

else :
    print("NO")




