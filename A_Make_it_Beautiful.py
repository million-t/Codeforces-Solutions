t = int(input())

for _ in range(t):
    n = int(input())

    nums = list(map(int, input().split()))

    nums.sort()
    if nums[-1] == nums[-2]:
        
        top = nums.pop()
        top_count = 0
        while nums and nums[-1] == top:
            top_count += 1
            nums.pop()

        nums.append(top)

        ans = sorted(nums, reverse=True)
        if not ans or ans[-1] == top:
            print('NO')

        else:
            print('YES')
            while top_count:
                ans.append(top)
                top_count -= 1

            print(*ans)    
    
    else:
        print('YES')
        print(*sorted(nums, reverse=True))

    
    
    
    

    

