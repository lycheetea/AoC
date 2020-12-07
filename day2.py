file = open("day2input", "r")
list = list(file.readlines())
list = [x.split() for x in list]
count = 0
def sendhelp(lyst):
    chuu = lyst[0]
    chuu = chuu.replace("-", " ")
    chuu = [int(i) for i in chuu.split()]
    lowchuu = chuu[0]
    hichuu = chuu[1]
    ryujin = lyst[1].replace(":", "")
    yeji = lyst[2]
    low = lowchuu - 1
    hi = hichuu - 1
    return (ryujin == yeji[low]) != (ryujin == yeji[hi])
    """boona = 0
     for x in yeji:
         if x==ryujin:
             boona = boona + 1
     return boona >= lowchuu and boona <= hichuu"""

for x in list:
    if sendhelp(x):
        count = count + 1
print(count)
