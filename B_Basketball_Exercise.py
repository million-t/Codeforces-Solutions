n = int( input())

h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))


for ind in range(1, n):

    h1[ind] = max(h1[ind  - 1], h1[ind] + h2[ind -1])
    h2[ind] = max(h2[ind  - 1], h2[ind] + h1[ind -1])

print(max(h1[-1], h2[-1]))
    