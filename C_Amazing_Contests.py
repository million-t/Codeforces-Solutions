n = int(input())
points = list(map(int, input().split(' ')))

amazing = 0
cur_min = points[0]
cur_max = points[0]

for i in range(1, n):

    if points[i] < cur_min:
        amazing += 1
        cur_min = points[i]

    elif points[i] > cur_max:
        amazing += 1
        cur_max = points[i]

print(amazing)
