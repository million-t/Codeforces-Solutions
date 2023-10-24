t = int(input())

for _ in range(t):
    n = int(input())
    monsters = list(map(int, input().split()))

    
    ones = monsters.count(1)
    spells = 0
    if not ones%2:
        spells += ones//2
    else:
        spells += ones//2 + 1
    
    spells += n - ones

    print(spells)

