file = open("day3input", "r")
list = file.readlines()
print(list)
tree = '#'
count = 0
treecount = 0
treecount1 = 0
treecount2 = 0
treecount3 = 0
treecount4 = 0
def tree_or_not(liszt, num):
    return tree == liszt[num]
#RIGHT 3 DOWN 1
for x in list:
    treeline = x.replace("\n", "")
    if tree_or_not(treeline, count):
        treecount = treecount + 1
    count = count + 3
    if count >= len(treeline):
        count = count - len(treeline)
print(treecount)
#RIGHT 1 DOWN 1
count = 0
for x in list:
    treeline = x.replace("\n", "")
    if tree_or_not(treeline, count):
        treecount1 = treecount1 + 1
    count = count + 1
    if count >= len(treeline):
        count = count - len(treeline)
print(treecount1)
#RIGHT 5 DOWN 1
count = 0
for x in list:
    treeline = x.replace("\n", "")
    if tree_or_not(treeline, count):
        treecount2 = treecount2 + 1
    count = count + 5
    if count >= len(treeline):
        count = count - len(treeline)
print(treecount2)
#RIGHT 7 DOWN 1
count = 0
for x in list:
    treeline = x.replace("\n", "")
    if tree_or_not(treeline, count):
        treecount3 = treecount3 + 1
    count = count + 7
    if count >= len(treeline):
        count = count - len(treeline)
print(treecount3)
#RIGHT 1 DOWN 2
count = 0
yes = True
for x in list:
    treeline = x.replace("\n", "")
    if yes:
        if tree_or_not(treeline, count):
            treecount4 = treecount4 + 1
        count = count + 1
        if count >= len(treeline):
            count = count - len(treeline)
    yes = not yes
print(treecount4)
print(treecount*treecount1*treecount2*treecount3*treecount4)