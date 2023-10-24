t = int(input())
for _ in range(t):
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))
    s1 =set(r1)
    s2 =set(r2)
    common = s1.intersection(s2)
    val = 0
    for item in common:
        val = item
    r1.remove(val)
    r2.remove(val)
    if len(common) != 1:
        print("No")
    elif r1 and r2 and r1[0] + r2[0] == val:
        print("Yes")
    else:
        print("No")

    

