

n = int(input())
a = list(map(int, input().split()))



ans = 0
state = [0, 0, 0]

for ind, num in enumerate(a):
    state[num] = 1

    
    
    if state[0] == 2:
        if state[2]:
            state = [0, 0, 0]
            ans += 1
        
        else:
            state = [1, 0, 0]
            ans += 1

if sum(state):
    ans += 1
        

print(ans)

            
