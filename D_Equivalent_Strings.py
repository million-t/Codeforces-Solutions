a = input()
b = input()



def helper(left, right, a, b):
    global a_rev
    if left >= right - 1:
        
        return True if a[left] == b[left] else False
    
    mid = left + (right - left)//2

    first_half = helper(left, mid, a, b)
    pos = helper(left, mid, a_rev, b)
    second_half = helper(mid, right, a, b)

    return first_half and second_half or pos and second_half

a_rev = a[::-1]

if helper(0, len(a), a, b):
    print('YES')

else:
    print('NO')

    
