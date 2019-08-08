def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        remainders = [n % i for i in range(2, n / 2)]
