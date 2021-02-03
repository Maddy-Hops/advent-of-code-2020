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

eye_colors = [
    "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
]
#checks if a string is a number, returns the number itself if correct, false if not
def is_number(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return False
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
    #if every field is present continue with checking
    if not isValid: continue
    #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    for i in headers:
        if i[0] == "byr":
            if byr := is_number(i[1]):
                if byr > 2002 or byr < 1920: 
                    isValid = False
                    break
            else:
                isValid = False
                break
        elif i[0] == "iyr":
            if iyr := is_number(i[1]):
                if iyr > 2020 or iyr < 2010: 
                    isValid = False
                    break
            else:
                isValid = False
                break
        elif i[0] == "eyr":
            if eyr := is_number(i[1]):
                if eyr > 2030 or eyr < 2020: 
                    isValid = False
                    break
            else:
                isValid = False
                break
        elif i[0] == "hgt":
            if hgt := is_number(i[1][:-2]):
                if i[1][-2:] == "cm":
                    if hgt > 193 or hgt < 150:
                        isValid = False
                        break
                elif i[1][-2:] == "in":
                    if hgt > 76 or hgt < 59:
                        isValid = False
                        break
                else:
                    isValid = False
                    break
            else:
                isValid = False
                break
        elif i[0] == "hcl":
            #check if hexadecimal 6 digit number
            if i[1][:1] == "#":
                if len(i[1][:1]) == 6:
                    try:
                        int(i[1][1:],16)
                    except ValueError:
                        isValid = False
                        break
            else:
                isValid = False
                break
        elif i[0] == "ecl":
            #if haven't encountered a color from the list - invalid
            for clr in eye_colors:
                if i[1] == clr: break
            else:
                isValid = False
                break
        elif i[0] == "pid":
            if len(i[1]) == 9:
                if not is_number(i[1]):
                    isValid = False
                    break
            else:
                isValid = False
                break
    if isValid: valid_passports += 1
print(valid_passports)