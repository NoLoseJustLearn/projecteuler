fibList = [1, 2]
fibNum = 3
while (fibNum < 4000000):
    fibList.append(fibNum)
    size = len(fibList)
    fibNum = fibList[size-2] + fibList[size-1]
total = 0
for i in fibList:
    if i%2 == 0:
        total = total+i
print(total)
