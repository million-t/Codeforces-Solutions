


s = input()
t = input()



n = min(len(s), len(t))
m = max(len(s), len(t))
x = 0

for ind in range(n):
    
    if s[~ind] != t[~ind]:
        break
    
    x += 1


print(m + n - 2*x )


