sum = 0
for i in range (3,999):
    if (i%3 == 0):
        sum = sum + i
    elif (i%5 == 0):
        sum = sum + i
print(sum)
