t = int(input())

for _ in range(t):
    n = int(input())

    nums = list(map(int, input().split()))
    nums.sort()

    blue_sum = nums[0]
    red_sum = 0
    left = 1   
    right = n - 1

    possible = False

    while left < right:
        red_sum += nums[right]
        blue_sum += nums[left]
        if red_sum > blue_sum:
            possible = True
            break
        
        left += 1
        right -= 1
         
    
    if possible:
        print('YES')
    
    else:
        print('NO')

