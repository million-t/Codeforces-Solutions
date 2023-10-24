from collections import Counter

t = int(input())
for _ in range(t):
    
    a, b = input().split()
    count = Counter(b)
    ans = 0

    for let in a:
        if not count[let]:
            break
        count[let] -= 1
        ans += 1

    print(ans)

