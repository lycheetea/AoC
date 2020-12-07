file = open("day6input", "r")
store = file.readlines()
store = list(x.replace("\n", "") for x in store)
pos = 0
count = 0
while pos < len(store):
    group = []
    pos_counter = 0
    for x in store[pos:]:
        pos_counter+=1
        if x == "":
            break
        group.extend(x.split())
    comp = set(group[0])
    for x in group:
        comp = comp.intersection(x)
    count += len(comp)
    pos += pos_counter
print(count)