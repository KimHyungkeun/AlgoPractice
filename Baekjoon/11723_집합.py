import sys

m = int(sys.stdin.readline())
user_sets = set({})

for _ in range(m) :
    user_input = sys.stdin.readline().rstrip()
    user_input = user_input.split(" ")

    if len(user_input) == 2 :
        cmd = user_input[0]
        x = int(user_input[1])

        if cmd == 'add' :
            if x not in user_sets :
                user_sets.add(x)
        elif cmd == 'remove' :
            if x in user_sets :
                user_sets.remove(x)
        elif cmd == 'check' :
            if x in user_sets :
                print(1)
            else :
                print(0)
        elif cmd == 'toggle' :
            if x in user_sets :
                user_sets.remove(x)
            else :
                user_sets.add(x)
        else :
            None
    else :
        cmd = user_input[0]
        if cmd == 'all' :
            for i in range(1, 21) :
                user_sets.add(i)
                
        elif cmd == 'empty' :
            user_sets = set({})
        else :
            None