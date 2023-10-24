



c = float(input())


def helper(x):
    return x**2 + x**0.5

start = 0
end = c**0.5

while start <= end:
    mid = start + (end - start)/2
    temp = helper(mid)
    if temp < c:
        start = mid + 0.0000001
    
    elif temp  > c:
        end = mid - 0.0000001
    
    else:
        print(mid)
        exit()

