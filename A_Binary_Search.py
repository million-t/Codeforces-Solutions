

n, k = map(int, input().split())
nums = list(map(int, input().split()))
queries = list(map(int, input().split()))


def search(nums, n, target):
    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] == target:
            return 'YES'
        
        elif nums[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return 'NO'
        





for num in queries:
    print(search(nums, n, num))