from tqdm import tqdm

distincts = []

for a in range(2, 101):
    for b in range(2, 101):
        c = a ** b
        if c not in distincts:
            distincts.append(c)

print(len(distincts))
