offset = [[1,1],[1,3],[1,5],[1,7],[2,1]]
treeMult = 1
data = []
with open("input.txt","r") as f:
    data = list(f)
data = [i.strip('\n') for i in data]
for i in offset:
    pos = 0
    print(i)
    treeCounter = 0
    for y in range(0,len(data),i[0]):
        if data[y][pos] == "#": treeCounter += 1
        pos += i[1]
        if pos > len(data[y])-1:
            pos -= len(data[0])
    else:
        treeMult *= treeCounter
        print(treeCounter)
print(treeMult)