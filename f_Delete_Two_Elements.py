from collections import defaultdict 
tests = int(input())

for _ in range(tests):

    n = int(input())
    nums = list(map(int, input().split()))

    average = sum(nums)/n
    target_sum = average*2
    
    dif_count = defaultdict(int)
    pairs = 0

    for num in nums:
        difference = target_sum - num
        pairs += dif_count[difference]
        dif_count[num] += 1
    
    print(pairs)