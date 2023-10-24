
def closest_to_the_right(pivot, nums, n):
    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left)//2
        cur = nums[mid]

        if cur < pivot:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return left

def closest_to_the_left(pivot, nums, n):

    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left)//2
        cur = nums[mid]

        if cur > pivot:
            right = mid - 1
        
        else:
            left = mid + 1

    return left

n = int(input())
a  = list(map(int, input().split()))
a.sort()
k = int(input())

queries = []
for line in range(k):
    queries.append(map(int, input().split()))


ans = []
for l, r in queries:
    ans.append(closest_to_the_left(r, a, n) - closest_to_the_right(l, a, n))

print(*ans)