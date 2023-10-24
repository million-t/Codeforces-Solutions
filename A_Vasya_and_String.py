

n, k = map(int, input().split())

s = input()

def solve(s, char, k, n):
    left = 0
    count = 0
    ans = 0
    for right in range(n):
        if s[right] != char:
            count += 1

        while left < right and count > k:
            count -= int(s[left] != char)
            left += 1
            

        ans = max(ans, right - left + 1)
    return ans

print(max(solve(s, 'a', k, n), solve(s, 'b', k, n)))

