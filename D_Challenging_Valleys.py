

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    temp = []
    for num in a:
        if temp and temp[-1] == num:
            continue
        
        temp.append(num)

    no = False
    for ind in range(1, len(temp) - 1):
        if temp[ind - 1] < temp[ind] > temp[ind + 1]:
            no = True
            break
 
    
    print('NO' if no else 'YES')