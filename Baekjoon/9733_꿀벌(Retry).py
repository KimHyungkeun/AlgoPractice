import sys

work_list = ["Re", "Pt", "Cc", "Ea", "Tb", "Cm", "Ex"]
group_work = {}
works = []

works = sys.stdin.readlines()

total = 0
for work in works :
    txt = list(work.split())
    for w in txt :
        if w not in group_work :
            group_work[w] = 1
        else :
            group_work[w] += 1
        total += 1
        

for work_type in work_list :
    if work_type not in group_work :
        print(work_type, 0, "{:.2f}".format(0.00))
    else :
        val = "{:.2f}".format(round(group_work[work_type] / total, 2))
        print(work_type, group_work[work_type], val)

print("Total", total, "{:.2f}".format(1.00))