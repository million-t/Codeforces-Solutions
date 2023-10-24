n = int(input())
nums = list(map(int, input().split()))



prev = 0
rests = 0


for num in nums:
    if not num:
        prev = 0
        rests += 1
    
    elif  num == 3:
        if prev:
            prev = 3 - prev

        continue

    else:
        if prev == num:
            rests += 1
            prev = 0
            continue

        else:
            prev = num
        

print(rests)
            

