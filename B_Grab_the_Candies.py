def sn(): return int(input())
def ln(): return map(int, input().split())
def lst(): return list(map(int, input().split()))

t = sn()

for _ in range(t):
    n = sn()
    nums = lst()

    evens = []
    odds = []
    for num in nums:
        if num%2:
            odds.append(num)
        
        else:
            evens.append(num)
    

    if sum(evens) > sum(odds):
        print('YES')
    
    else:
        print('NO')
