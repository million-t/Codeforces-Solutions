first, second = map(int, input().split())

minutes = 0
while first > 0 and second > 0:
    if first == second == 1:
        break
    if first < second:
        first += 1
        second -= 2
    
    else:
        first -= 2
        second += 1

    minutes += 1

print(minutes)
