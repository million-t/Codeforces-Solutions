from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count_a = Counter(a)
count_b = Counter(b)

ans = 0
for num in set(a):
    ans += count_a[num]*count_b[num]


print(ans)