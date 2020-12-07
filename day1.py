file = open("day1input", "r")
list = list(file.readlines())
list = [int(x) for x in list]
lol = False
for x in list:
    for y in list:
        for z in list:
            if x+y+z==2020:
                print(x*y*z)
                lol = True
            if lol:
                break
        if lol:
            break
    if lol:
        break