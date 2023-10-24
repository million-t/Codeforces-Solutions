t = int(input())

for _ in range(t):
    n, s = map(int, input().split())

    transactions = list(map(int, input().split()))


    amount = s
    max_width = [-1]
    width = [0, 0]

    for i, tr in enumerate(transactions):
        if amount + tr > -1:
            amount += tr
            width[1] += 1
        
        else:
            if len(max_width) == 1 or width[1] - width[0] > max_width[1] - max_width[0]:
                max_width = width
            amount = s
            width = [i, i]
        
    
    print(max_width)
