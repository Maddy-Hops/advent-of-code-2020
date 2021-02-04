import time
start = time.time()
with open("input.txt","r") as f:
    data = [x.strip("\n") for x in f.readlines()]
accumulator = 0
i = 0
ran_instructions = []
while True:
    ran_instructions.append(i)
    instruction = data[i]
    if  instruction[:3] == "acc": 
        accumulator += int(instruction[4:])
        i += 1
    elif instruction[:3] == "jmp": 
        i += int(instruction[4:])
    else:
        i += 1
    if i in ran_instructions:
        print("ACC is: ", accumulator)
        print("Last instruction ran: ", i)
        break
#part2
i_to_change = 0
old_data = data.copy()
while True:
    accumulator = 0
    i = 0
    ran_instructions = []
    if data[i_to_change][:3] == "acc":
        i_to_change += 1
        continue
    if data[i_to_change][:3] == "jmp":
        data[i_to_change] = data[i_to_change].replace("jmp","nop")
    elif data[i_to_change][:3] == "nop":
        data[i_to_change] = data[i_to_change].replace("nop","jmp")
    while True:
        ran_instructions.append(i)
        instruction = data[i]
        if  instruction[:3] == "acc": 
            accumulator += int(instruction[4:])
            i += 1
        elif instruction[:3] == "jmp": i += int(instruction[4:])
        else: i += 1
        if i in ran_instructions: 
            break
        if i == len(data):
            print("Accumulator is: ", accumulator)
            print("Success")
            end = time.time()
            print("Execution time: ", ((end - start)*1000000//10/100)," ms")
            exit()
    data = old_data.copy()
    i_to_change += 1