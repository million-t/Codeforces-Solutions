from collections import Counter
t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    count = Counter(a)

    cost = 0
    for num, freq in count.items():
        if freq >= c:
            cost += c

        else:
            cost += freq 


    print(cost)