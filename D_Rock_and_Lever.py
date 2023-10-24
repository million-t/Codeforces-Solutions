
from collections import defaultdict

t = int(input())






for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))


    left_most = [num.bit_length() for num in nums]

    count = defaultdict(int)
    valid = 0

    for val in left_most:
        valid += count[val]
        count[val] += 1
    
    print(valid)