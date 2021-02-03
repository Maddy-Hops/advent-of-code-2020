required_fields = [
    "byr", 
    "iyr", 
    "eyr", 
    "hgt",
    "hcl", 
    "ecl", 
    "pid", 
    #"cid"
    ]
#dump all contents into a string
with open("input.txt","r") as f:
    temp = f.read()
#each separate passport is delimited by 2 newline chars
#put every passport in a list
data = temp.split(sep="\n\n")
#replace newlines with spaces inside of every passport description
data = [i.replace('\n',' ') for i in data]
valid_passports = 0
for passport in data:
    #split passport into separate fields(with a space)
    fields = passport.split()
    headers = []
    for field in fields:
        headers.append(field.split(sep=":"))
    #merge nested lists into one
    temp = []
    for header in headers: temp += header
    #go through our list of headers and info and check against the req
    isValid = True
    for i in required_fields:
        flag = False
        for j in temp:
            if i == j: flag = True
        #if there is even one req field missing - abort
        if not flag: 
            isValid = False
            break
    #if every field is present increase the count
    if isValid: valid_passports += 1
print(valid_passports)