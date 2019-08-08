# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

found = 0
primeProduct = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
num = primeProduct

while found == 0:
    found = 1
    print(num)
    for i in range(1, 20):
        if num % i > 0:
            found = 0
    num += primeProduct

print("Solution: ", num)
