file = open("day5input", "r")
store = file.readlines()
store = list(x.replace("\n", "") for x in store)
def row(inp):
    lower = 0
    upper = 127
    for x in inp[:6]:
        if x == "F":
            upper = (upper + lower)/2 - 0.5
        if x == "B":
            lower = (upper + lower)/2 + 0.5
    if inp[6] == "F":
        return int(lower)
    else:
        return int(upper)

def column(inp):
    something = inp[6:]
    lower = 0
    upper = 7
    for x in something[:3]:
        if x == "L":
            upper = (upper + lower) / 2 - 0.5
        if x == "R":
            lower = (upper + lower) / 2 + 0.5
    if inp[-1] == "L":
        return int(lower)
    else:
        return int(upper)

high_id = 0
id_list = []
for x in store:
    seatID = row(x)*8 + column(x)
    if seatID > high_id:
        high_id = seatID
    id_list.append(seatID)
print(high_id)
id_list.sort()
start_id = id_list[0] - 1

for x in id_list:
    if x != start_id + 1:
        print(x-1)
        break
    start_id = x
