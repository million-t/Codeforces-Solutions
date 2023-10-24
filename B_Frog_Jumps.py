


t = int(input())

for _ in range(t):
    s = input()


    ans = 0
    left = 0
    for ind, char in enumerate(s):
        if char == 'R':
           ans = max(ans, ind + 1 - left)
           left = ind + 1

    ans = max(ans, len(s) + 1 - left)
    print(ans) 
