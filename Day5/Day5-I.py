with open("input.txt","r") as f:
    data = [x.strip("\n") for x in f.readlines()]
boardingPasses = []
for boardingPass in data:
    row, column = 0, 0
    left,right = 0, 127
    for i in range(6):
        mid = (left+right)//2
        if boardingPass[i] == "B": left = mid+1
        else: right = mid
    if boardingPass[6] == "B": row = right
    else: row = left
    left, right = 0, 7
    for i in range(7,9):
        mid = (left+right)//2
        if boardingPass[i] == "R": left = mid+1
        else: right = mid
    if boardingPass[9] == "R": column = right
    else: column = left
    seatID = row * 8 + column
    boardingPasses.append(seatID)
print("Highest seatID: ",max(boardingPasses))
missingPasses = []
for i in range(0,1024):
    if i not in boardingPasses: missingPasses.append(i)
for i in missingPasses:
    if i+1 in boardingPasses and i-1 in boardingPasses: print("My seatID is:   ",i)