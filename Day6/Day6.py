with open("input.txt","r") as f:
    data = [x.strip("\n") for x in f.readlines()]
count = 0
group = set()
for i in data:
    if i: group = group.union(i)
    if not i:
        count+=len(set(group))
        group = set()
print(count)
#part 2
j = 0
count = 0
group = set(data[0])
for i in data:
    if i: group = group.intersection(i)
    if not i:
        count+=len(group)
        if j+1 < len(data): group = set(data[j+1])
    j += 1
print(count)