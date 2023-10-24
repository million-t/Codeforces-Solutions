

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))


passed = set(x[1:] + y[1:])

print("I become the guy." if len(passed) == n else "Oh, my keyboard!")