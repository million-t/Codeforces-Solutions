





def solve(nums, n , k):
    
    remainings = [0]*n
    for i, num in enumerate(nums):
        remainings[i] = k - (num%k)
    
    remainings.sort()
    
    ind = 0
    ops = 0
    while ind < n:

        rem_val = remainings[ind]
        factor = 0

        ind += 1
        while ind < n and remainings[ind - 1] == remainings[ind]:
            factor += 1
            ind += 1
        
        if rem_val != k:
            ops = max(ops, rem_val + k*factor + 1)


    return ops



t = int(input())


for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve(nums, n, k))
