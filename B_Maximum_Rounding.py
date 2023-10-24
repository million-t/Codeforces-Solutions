

t = int(input())
for _ in range(t):
    x = input()

    temp = [0]
    for char in x:
        temp.append(int(char))

    sc = len(x)

    ind = len(temp) - 2
    overflow = False

    while ind > -1:
        if temp[ind] < 9 and temp[ind + 1] >= 5:
            temp[ind] += 1
            ind -= 1
            sc = ind + 1
        elif temp[ind + 1] >= 5:
            
            while ind > -1 and temp[ind] == 9:
                ind -= 1
            
            if ind > -1:
                temp[ind] += 1
                ind -= 1
                sc = ind + 1
            
            else:
                overflow = True
            
        else:
            ind -= 1
            
    
    if overflow:
        ans = [[0]*(len(temp) + 1)]
        ans[0] = 1
        
        print(''.join(map(str, ans)))
    
    else:
        ans = [0]*len(temp)
        for i in range(sc + 1):
            ans[i] = temp[i]
        
        print( str(int(''.join(map(str, ans)))))
        

