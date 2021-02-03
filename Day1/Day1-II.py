data = []
with open("input.txt","r") as f:
    data = list(f)
for i in data:
    for j in data:
        for k in data:
            if int(i)+int(j)+int(k) == 2020: 
                print(int(i)*int(j)*int(k))
                exit()