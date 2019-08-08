# Calculate the score of the path
def scorePath(path, tree):
    score = 0
    xcoord = 0
    for i in range(0, len(path)):
        if path[i] == 1:
            xcoord += 1
        score += int(tree[i][xcoord][0])
    print(score)
    return score


# Returns the next path
def nextPath(path):
    path.reverse()
    for i in range(0, len(path)):
        if path[i] == 0:
            path[i] = 1
            break
        else:
            path[i] = 0
    path.reverse()
    return path


def lastPath(path):
    for i in range(1, len(path)):
        if path[i] == 0:
            return 0
    return 1


tree = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

tree = list(tree)

while tree.count(" ") > 0:
    tree.remove(" ")

rows = 15
formTree = []
row = []

# Format tree into matrix
for i in range(rows + 1):
    for j in range(0, i):
        tempStr = ["".join(tree[0:2])]
        row.append(tempStr)
        del tree[0]
        del tree[0]
    print(row)
    formTree.append(row)
    row = []
del formTree[0]

highscore = 0

# Define path list
path = []
for i in range(rows):
    path.append(0)

print(formTree[0][0])
while lastPath(path) == 0:
    pathScore = scorePath(path, formTree)
    if pathScore > highscore:
        highscore = pathScore
        print(highscore)
    print(path)
    path = nextPath(path)
print(highscore)
