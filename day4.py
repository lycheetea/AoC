file = open("day4input", "r")
leest = file.readlines()
print(leest)
pos = 0
count = 0
while pos < len(leest):
    passport = []
    pos_counter = 0
    for x in leest[pos:]:
        pos_counter += 1
        if x == '\n':
            break
        passport.extend(x.split())
    counter = 0
    hcl_list = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in passport:
        if x[:3] == 'byr':
            byear = int(x[4:])
            if byear >= 1920 and byear <= 2002:
                counter+=1
        if x[:3] == 'iyr':
            iyear = int(x[4:])
            if iyear >= 2010 and iyear <= 2020:
                counter+=1
        if x[:3] == 'eyr':
            eyear = int(x[4:])
            if eyear >= 2020 and eyear <= 2030:
                counter+=1
        if x[:3] == 'hgt':
            height = x[4:]
            if height.endswith('in'):
                height1 = int(height.replace('in', ''))
                if 59 <= height1 <= 76:
                    counter+=1
            if height.endswith('cm'):
                height1 = int(height.replace('cm', ''))
                if 150 <= height1 <= 193:
                    counter+=1
        if x[:3] == 'hcl':
            hcolor = x[4:]
            if hcolor[0]=='#':
                hcolor = hcolor[1:]
                if len(hcolor)==6:
                    hclproof = [characters in hcl_list for characters in hcolor]
                    hclfinal = all(hclproof)
                    if hclfinal:
                        counter+=1
        if x[:3] == 'ecl':
            if x[4:] == 'amb' or x[4:] == 'blu' or x[4:] == 'brn' or x[4:] == 'gry' or x[4:] == 'grn' or x[4:] == 'hzl' or x[4:] == 'oth':
                counter+=1
        if x[:3] == 'pid':
            passid = x[4:]
            if len(passid) == 9 and passid.isnumeric():
                counter+=1
    if counter == 7:
        count +=1
    pos += pos_counter
print(count)

