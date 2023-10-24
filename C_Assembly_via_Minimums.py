from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    count = Counter(b)
    temp = []
    for num, freq in count.items():
        temp.append((num, freq))

    temp.sort(reverse = True)
    ans = []
    k = 1
    for num, freq in temp:
        while freq > 0:
            freq -= k
            k += 1
            ans.append(num)
        
        # k += 1

    ans.append(max(ans))
    
    print(*ans)