n = input()
m = input()


digs = []
for dig in n:
    digs.append(dig)

digs.sort( reverse = True)

zeros = []
while digs and digs[-1] == '0':
    zeros.append(digs.pop())

if not digs:
    
    if m == '0':
        print('OK')
    
    else:
        print('WRONG_ANSWER')

else:
    ans = [digs.pop()]
    
    for num in zeros:
        ans.append(num)
    
    while digs:
        ans.append(digs.pop())
    
    
    num = ''.join(ans)
    if m == num:
        print('OK')
    
    else:
        print('WRONG_ANSWER')
     