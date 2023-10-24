n = int(input())
arr = list(map(int, input().split()))

set1 = set()
set2 = set()
set3 = set()
indx0 = arr.index(0)
arr.sort()

for i in range(n):
    if i == 0 and arr[i]<0:
        set1.add(arr[i])
    elif i == 1 and indx0%2==0:
        set2.add(arr[i])
    elif arr[i] == 0:
        set2.add(arr[i])
    else:
        set3.add(arr[i])
print(str(len(set1)) +' '+ ' '.join(map(str, list(set1))))

print(str(len(set3)) +' '+ ' '.join(map(str, list(set3))))
print(str(len(set2)) +' '+ ' '.join(map(str, list(set2))))