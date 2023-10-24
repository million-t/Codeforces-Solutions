from bisect import bisect_left

n, m = map(int, input().split())

students = list(map(int, input().split()))
students.sort()
for _ in range(n):
    quest = int(input())
    pos = bisect_left(students, quest)

    if ((m%2 and pos < m//2 + 1) or (pos < m//2)) and pos != 0:
        print('YES')
    
    else:
        print('NO')

