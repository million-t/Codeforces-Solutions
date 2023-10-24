from collections import defaultdict
tests = int(input())

for _ in range(tests):
    n = int(input())
    digits = input()
    
    prefix = [0]
    for dig in digits:
        prefix.append(prefix[-1] + int(dig) - 1)

    # print(prefix)
    count = defaultdict(int)
    good = 0

    for pre in prefix:
        good += count[pre]
        count[pre] += 1
    
    print(good)

    