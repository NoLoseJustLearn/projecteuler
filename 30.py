i = 10
full_sum = 0

while True:
    i += 1
    dig_sum = sum((int(dig) ** 5 for dig in str(i)))
    if dig_sum == i:
        full_sum += dig_sum
        print(f"Bingo! New sum: {full_sum}")
