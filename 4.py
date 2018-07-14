maxNum = 0

def isPal(num):
    list = []
    digCount = len(str(num))
    for i in range (0,digCount):
        list.append(num%10)
        num = num/10

    if list == list[::-1]:
        return 1
    else:
        return 0
        
if (isPal(1002)==0):
    print("Success?")
if (isPal(1001)==1):
    print("Succes!")

for i in range(100,999):
    for j in range(100,999):
        testNum = i*j
        if (isPal(testNum)==1):
            if (testNum>maxNum):
                print(testNum)
                maxNum = testNum
