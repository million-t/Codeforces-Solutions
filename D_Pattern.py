from collections import defaultdict
def countQmarks(lst):
    count = 0
    place_holder = ''
    for val in lst:
        if val == '?':
            count += 1
        else:
            place_holder = val

    return [count, place_holder]

n = int(input())

indx_letters = defaultdict(list)
for _ in range(n):
    word = input()
    
    for ind, char in enumerate(word):
        indx_letters[ind].append(char)
#print(indx_letters)
max_intersect = 0
ans = ''
for itm in indx_letters.values():
    q_marks = countQmarks(itm)
    max_intersect = max(max_intersect, q_marks[0])
    
    if q_marks[0] == n:
        ans+='x'
    
    elif q_marks[0] == 0 and max_intersect == 0:
        ans+='?'

    else:
        ans+=q_marks[1]
print(ans)
    
    