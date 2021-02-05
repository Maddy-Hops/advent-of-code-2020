import time
start = time.time()
with open("/home/maddy/Documents/AoC-2020/Day10/input.txt","r") as f:
    data = [int(x.strip("\n")) for x in f.readlines()]
difference = [3]
data.sort()
data.append(max(data)+3)
data.insert(0,0)
for i in range(len(data)-1):
    difference.append(data[i+1]-data[i])
print(difference.count(1) * difference.count(3))
#part2
def recursiveWalk(dat, n, paths):
    if n == max(dat):
        paths[0] += 1
        return 
    for i in range(1,4):
        if n+i in dat:
            recursiveWalk(dat,n+i,paths)
n_data = []
i = 0
while data[i] != max(data):
    isNewList = True
    tmp = [data[i]]
    while isNewList:
        for j in range(1,3):
            if data[i] + j in data:
                tmp.append(data[i]+j)
                break
        else:
            isNewList = False
            n_data.append(tmp)
        i += 1
result = 1
for i in n_data:
    paths = [0]
    recursiveWalk(i,i[0],paths)
    result *= paths[0]
print(result)
end = time.time()
print("Execution time: ", ((end - start)*1000000//10/100)," ms")