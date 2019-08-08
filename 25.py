fib_index = 2
current_num = 2
f_dict = {1: 1, 2: 1, 3: 2}

while len(str(f_dict[fib_index])) < 1000:
    fib_index += 1
    f_dict[fib_index] = f_dict[fib_index - 1] + f_dict[fib_index - 2]
    print(len(str(f_dict[fib_index])))

print(fib_index)
