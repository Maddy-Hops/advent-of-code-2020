data = []
with open("input.txt","r") as f:
    data = list(f)
for i in data:
    for j in data:
        if int(i)+int(j) == 2020: 
            print(int(i)*int(j))
            exit()
