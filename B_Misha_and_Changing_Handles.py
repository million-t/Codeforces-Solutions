

q = int(input())
queries = []
temp = {}

for _ in range(q):
    a, b = input().split()
    
    if a in temp:
        temp[b] = temp.pop(a)
    else:
        temp[b] = a

print(len(temp))
for a, b in temp.items():
    print(b, a)
