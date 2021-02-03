import itertools
import time

start = time.time()
print("Timer started")
def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#recursively searches for every color that can hold s color bags and adds them to the list
def recursiveSearch(s):
    if type(s) != type(list()): 
        answer.add(s)
        #exit condition
        if s in unholdableColors:
            return True
        else:
            return recursiveSearch([x for x in colors if s in colors[x]])
    else:
        for i in s:
            answer.add(i)
            recursiveSearch(i)

with open("input.txt","r") as f:
    data = [x.strip("\n") for x in f.readlines() if "contain no other bags." not in x]

colors = dict()
#prepare a dictionary of all the colors
for rule in data:
    rule = rule.split()
    rule = [
    x.strip(", ").strip(".") for x in rule 
    if x.strip(", ").strip(".") != "bag" 
    and x.strip(", ").strip(".") != "bags" 
    and x.strip(", ").strip(".") != "contain" 
    and not isNumber(x.strip(", ").strip("."))
    ]
    tmp = []
    for i in range(0,len(rule),2):
        tmp.append(rule[i]+rule[i+1])
    rule = tmp
    colors[rule[0]] =  [x for x in rule[1:]]
tmp = [i for i in colors.values()]
listOfAllValues = list(itertools.chain(*tmp))

#prepare a list of colors THAT CANNOT BE HELD INSIDE ANY OTHER BAGS
unholdableColors = [i for i in colors if i not in listOfAllValues]

answer = set()
recursiveSearch("shinygold")
print(len(answer)-1)

#part2

colors = dict()
#prepare a dictionary of all the colors but with numbers this time
for rule in data:
    rule = rule.split()
    rule = [
    x.strip(", ").strip(".") for x in rule 
    if x.strip(", ").strip(".") != "bag" 
    and x.strip(", ").strip(".") != "bags" 
    and x.strip(", ").strip(".") != "contain" 
    ]
    tmp = [rule[0]+rule[1]]
    for i in range(2,len(rule),3):
        tmp.append(rule[i]+rule[i+1]+rule[i+2])
    rule = tmp
    colors[rule[0]] = [x for x in rule[1:]]
#returns the number of bags required to fill an s bag
def recursiveCount(s):
    if s not in colors:
        return 1
    secondaryBags = [x for x in colors[s]]
    c = 1
    for x in secondaryBags:
        c += int(x[0]) * recursiveCount(x[1:])
    else: return c
print(recursiveCount("shinygold")-1)
end = time.time()
print("Execution time: ", ((end - start)*1000000//10/100)," ms")