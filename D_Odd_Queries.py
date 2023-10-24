t = int(input())

def solve(arr, n, l, r, k, _sum):
    sub_sum = arr[r] - arr[l - 1]

    if (_sum - sub_sum + k*(r - l + 1))%2:
        return 'YES'

    return 'NO' 

    



for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)


    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().split())))
    
    for l, r, k in queries: 
        print(solve(prefix, n, l, r, k, prefix[-1]))
