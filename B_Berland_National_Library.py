

n = int(input())
temp = []
for _ in range(n):
    sign, num = input().split()
    num = int(num)
    temp.append((sign, num))





count = {}
a = 0
for ind in range(n):
    sign, num = temp[ind]
    
    if sign == '+':
        count[num] = 1
        a = max(len(count), a)
        
    else:
        if num in count:
            count.pop(num)
        
        else:
            a += 1

print(a)
