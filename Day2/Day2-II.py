data = []
with open("input.txt","r") as f:
    data = list(f)
numOfValidPassword = 0
for elem in data:
    low, high = "",""
    cutoff = 0
    for i in elem:
        cutoff += 1
        if i == "-": 
            break
        low += i
    for i in elem[cutoff:]:
        cutoff += 1
        if i == " ": 
            break
        high += i
    low,high = int(low),int(high)
    key = elem[cutoff]
    #add two because after the key there's always a colon and then a space before the actual password
    cutoff += 2
    password = elem[cutoff:-1]
    flag = False
    if password[low] == key: flag = not flag
    if password[high] == key: flag = not flag
    if flag: numOfValidPassword += 1
print(numOfValidPassword)