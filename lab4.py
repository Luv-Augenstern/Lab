from itertools import combinations


items = [
    ('r','rifle', 3, 25),
    ('p','pistol',2,15),
    ('a','ammo',  2,15),
    ('m','medkit',2,20),
    ('i','inhaler',1,5),
    ('k','knife',1,15),
    ('x','axe',3,20),
    ('t','talisman',1,25),
    ('f','flask',1,15),
    ('d','antidote',1,10),  # He has paranoia so he must take the antidote
    ('s','supplies',2,20),
    ('c','crossbow',2,20)
]

BACKPACK_SIZE = 9 # 3x3
BASIC_POINTS = 15
NECESSARY_ITEM = ['d']

# Calculate the value of all items
total_all = 0
for it in items:
    total_all += it[3]

# Find the best combination
best = ([], float('-inf'))
n = len(items)

for r in range(n+1):
    for combo in combinations(range(n), r):
        # Check whether to take the antidote
        if NECESSARY_ITEM:
            HAS_NECESSARY_ITEM = all(any(items[i][0] == item for i in combo) for item in NECESSARY_ITEM)
            if not HAS_NECESSARY_ITEM:
                continue # Lack of necessary item,skip this round

        # Calculate the size of the combination
        size = sum(items[i][2] for i in combo)
        if size > BACKPACK_SIZE:
            continue # Exceed the size of the backpack,skip this round

        # Calculate the value of the combination
        val = sum(items[i][3] for i in combo)
        if val > best[1]:
            best = (list(combo), val)

# Formula
chosen, sum_taken = best
final = BASIC_POINTS + 2 * sum_taken - total_all

# Backpack
cells = []
for i in chosen:
    cells += [items[i][0]] * items[i][2]
cells += ['.'] * (BACKPACK_SIZE - len(cells))

# 3x3
rows = [cells[i*3:(i+1)*3] for i in range(3)]

# Result
print("necessary item:", NECESSARY_ITEM)
print("chosen items:")
for i in chosen:
    print(items[i])
print("\nbackpack (3x3):")
for r in rows:
    print(', '.join(f'[{x}]' for x in r))
print(f"\nsum_taken={sum_taken}")
print(f"final_score={final}")