pos = 0
offset = 3
treeCounter = 0
with open("input.txt","r") as f:
    while line := f.readline().rstrip('\n'):
        if line[pos] == "#": treeCounter += 1
        pos += offset
        if pos > len(line)-1: pos -= len(line)
print(treeCounter)