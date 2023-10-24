m = int(input())
b = sorted(list(map(int, input().split())))
n = int(input())
g = sorted(list(map(int, input().split())))

p1 = 0
count = 0
for i in range(n):
    while p1 < m and b[p1] < g[i] - 1:
        p1 += 1

    if p1 < m and b[p1] - g[i] in [-1, 0, 1]:
        count += 1
        p1 += 1
     
    

print(count)  
    