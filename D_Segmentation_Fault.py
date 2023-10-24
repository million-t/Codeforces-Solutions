

t = int(input())
for _ in range(t):
    n = int(input())


    _max = []
    if n & 1:
        _max.append('7')

        for i in range(3, n, 2):
            _max.append('1')
    
    else:
        for i in range(0, n, 2):
            _max.append('1')
    
    temp = [8, 0, 2, 4, 7, 1]
    _map = {
        7: '8',
        6: '0',
        5: '2',
        4: '4',
        3: '7',
        2: '1'
    }
    
    print(int(''.join(_min)), int(''.join(_max)))


