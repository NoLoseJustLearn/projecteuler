num = 600851475143

i = 2
bot = 2
while(i<num):
    if (num%i==0):
        num = num/i
        print (num)
        i = 2
    i = i + 1
    bot = i
