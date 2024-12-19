
with open('one.csv') as input:
    left: list = []
    right: list = []
    for line in input:
        row = line.split()
        left.append(row[0])
        right.append(row[1])

left.sort()
right.sort()
difference = 0

similarity_score = 0
for leftN in left:
    matches = 0
    for rightN in right:
        if rightN == leftN:
            matches += 1
    similarity_score = similarity_score + matches * int(leftN)

print(similarity_score)








