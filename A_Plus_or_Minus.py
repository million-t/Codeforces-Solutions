def sn(): return int(input())
def ln(): return map(int, input().split())
def lst(): return list(map(int, input().split()))

t = sn()
for _ in range(t):
    a, b, c = ln()

    if a + b == c:
        print('+')
    
    else:
        print('-')