lefties = {}
updates = []
sum_of_mid = 0

with open('five_1.csv') as ordering_rules:
    for line in ordering_rules.readlines():
        left, right = map(int, line.strip().split('|'))  # Ensure no trailing newline issues
        lefties.setdefault(left, []).append(right)

with open('five_2.csv') as updates_input:
    for line in updates_input.readlines():
        updates.append(list(map(int, line.strip().split(','))))


for update in updates:
    valid = True
    for i in range(len(update) - 1, -1, -1):
            previous = update[:i]
            order = lefties.get(update[i])
            if any(page in order for page in previous):
                valid = False
                break
            if not valid:
                break
    if valid:
        sum_of_mid+=update[len(update)//2]


print(sum_of_mid)


