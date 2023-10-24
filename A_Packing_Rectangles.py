
def helper(size, w, h, n):
    vert = size // h
    horiz = size // w

    if vert*horiz >= n:
        return True
    
    return False




w, h, n = map(int, input().split())



start = 1
end = max(w*n, h*n)

while start <= end:
    mid = start + (end - start)//2

    if helper(mid, w, h, n):
        end = mid - 1
    
    else:
        start = mid + 1

print(start)
