

t = int(input())

for _ in range(t):

    s = input()
    yes = True
    left = 0

    temp = []

    right = 0
    while right < len(s):
        left = right
        
        while right < len(s) and s[left] == s[right]:
            right += 1

        temp.append(right - left)
    
    for num in temp:
        if num <= 1:
            yes = False
            break
    
    if yes:
        print('YES')
    
    else:
        print('NO')