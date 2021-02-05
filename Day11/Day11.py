import os
import time
import copy
occupied = '#'
empty = 'L'

def checkState(i,j,data):
    occupiedSeats = 0
    #check vertically
    if data[i+1][j] == occupied: occupiedSeats += 1
    if data[i-1][j] == occupied: occupiedSeats += 1
    #check horizontally
    if data[i][j+1] == occupied: occupiedSeats += 1
    if data[i][j-1] == occupied: occupiedSeats += 1
    #check diagonally
    if data[i+1][j+1] == occupied: occupiedSeats += 1
    if data[i+1][j-1] == occupied: occupiedSeats += 1
    if data[i-1][j+1] == occupied: occupiedSeats += 1
    if data[i-1][j-1] == occupied: occupiedSeats += 1
    return occupiedSeats

def run(limit):
    with open("/home/maddy/Documents/AoC-2020/Day11/input.txt","r") as f:
        data = [x.strip("\n") for x in f.readlines()]
    #add floor tiles all around our input for ease of checking
    for i in range(len(data)):
        data[i] = ''.join(('.',data[i],'.'))
    data.insert(0,'.'*len(data[0]))
    data.append('.'*len(data[0]))
    for i in range(len(data)):
        data[i] = list(data[i])
    hasChanged = True
    changes = 0
    while hasChanged:
        if changes == 1: pass
        n_data = copy.deepcopy(data)
        hasChanged = False
        for i in range(1,len(data)-1):
            for j in range(1,len(data[i])-1):
                seat = data[i][j]
                occupiedSeats = checkState(i,j,data)
                if seat == occupied and occupiedSeats >= limit: 
                    n_data[i][j] = empty
                    hasChanged = True
                if seat == empty and occupiedSeats == 0: 
                    n_data[i][j] = occupied
                    hasChanged = True
        data = copy.deepcopy(n_data)
    changes += 1
    occupiedSeats = 0
    for i in data:
        occupiedSeats += i.count(occupied)
    print(occupiedSeats)

run(4)
#part 2
def checkState(i,j,data):
    occupiedSeats = 0
    #check vertically
    k = 1
    while i + k < len(data):
        if data[i+k][j] == occupied:
            seat = data[i+k][j]
            occupiedSeats += 1
            break
        elif data[i+k][j] == empty:
            break
        k += 1
    k = 1
    while i - k >= 0:
        if data[i-k][j] == occupied: 
            occupiedSeats += 1
            break
        elif data[i-k][j] == empty:
            break
        k += 1
    #check horizontally
    k = 1
    while j + k < len(data[i]):
        if data[i][j+k] == occupied: 
            occupiedSeats += 1
            break
        elif data[i][j+k] == empty:
            break
        k += 1
    k = 1
    while j - k >= 0:
        if data[i][j-k] == occupied: 
            occupiedSeats += 1
            break
        elif data[i][j-k] == empty:
            break
        k += 1
    #check diagonally
    k = 1
    while i + k < len(data) and j + k < len(data[i]):
        if data[i+k][j+k] == occupied: 
            occupiedSeats += 1
            break
        elif data[i+k][j+k] == empty:
            break
        k += 1
    k = 1
    while i + k < len(data) and j - k >= 0:
        if data[i+k][j-k] == occupied: 
            occupiedSeats += 1
            break
        elif data[i+k][j-k] == empty:
            break
        k += 1
    k = 1
    while i - k >= 0 and j + k < len(data[i]):
        if data[i-k][j+k] == occupied: 
            occupiedSeats += 1
            break
        elif data[i-k][j+k] == empty:
            break
        k += 1
    k = 1
    while i - k >= 0 and j - k >= 0:
        if data[i-k][j-k] == occupied: 
            occupiedSeats += 1
            break
        elif data[i-k][j-k] == empty:
            break
        k += 1
    return occupiedSeats
run(5)