def isPrime(num):
    print("Prime Check:", num)
    maxDiv = int(num / 2)
    for i in range(2, maxDiv):
        if num % i == 0:
            return 0
    return 1


primeCount = 5
num = 12

while primeCount < 10001:
    num = num + 1
    if isPrime(num) == 1:
        primeCount = primeCount + 1
        print(primeCount)
print(num)
