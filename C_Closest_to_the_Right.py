

n, k = map(int, input().split())
nums = list(map(int, input().split()))
pivots = list(map(int, input().split()))



for pivot in pivots:
    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left)//2
        cur = nums[mid]

        if cur < pivot:
            left = mid + 1
        
        else:
            right = mid - 1
        
    
    print(left + 1)