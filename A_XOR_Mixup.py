t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    

    for i in range(n):
        x = nums[i]
        xor = 0
        for j in range(n):
            if j == i:
                continue

            xor ^= nums[j]
        
        if xor == x:
            print(x)
            break