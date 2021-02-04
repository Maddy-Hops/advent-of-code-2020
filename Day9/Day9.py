import time
import collections

start = time.time()

queue_size = 25

with open("/home/maddy/Documents/AoC-2020/Day9/input.txt","r") as f:
    data = [int(x.strip("\n")) for x in f.readlines()]
q = collections.deque(maxlen=queue_size)
for i in range(queue_size):
    q.append(data[i])
i = queue_size
weakness = 0
while True:
    new_item = data[i]
    for j in range(queue_size):
        if new_item - q[j] in q:
            q.append(new_item)
            break
    else:
        weakness = new_item
        break
    i += 1
j = 0
while True:
    i = j
    contig_sum = []
    while sum(contig_sum) <  weakness:
        contig_sum.append(data[i])
        i += 1
    j += 1
    if sum(contig_sum) != weakness: 
        continue
    else:
        print(min(contig_sum)+max(contig_sum))
        break


end = time.time()
print("Execution time: ", ((end - start)*1000000//10/100)," ms")
exit()

