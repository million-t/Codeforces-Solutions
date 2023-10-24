def sn(): return int(input())
def ln(): return map(int, input().split())
def lst(): return list(map(int, input().split()))

n = sn()
ax, ay = ln()
bx, by = ln()
cx, cy = ln()

def inbound(x, y):
    global n
    return 1 <= x <= n and 1 <= y <= n

def check(x, y):
    global ax, ay

    if ax == x or ay == y or ax - x == ay - y or x + y == ax + ay:
        return True
    
    return False

directions = [(0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (1, 0), (-1, 0), (-1, -1)]

stack = [(bx, by)]
visited = set([(bx, by)])
yes = False

while stack:
    cur_x, cur_y = stack.pop()

    if (cur_x, cur_y) == (cx, cy):
        yes = True
        break

    for change_x, change_y in directions:
        new_x = cur_x + change_x
        new_y = cur_y + change_y

        if inbound(new_x, new_y) and (not check(new_x, new_y)) and (new_x, new_y) not in visited:
            stack.append((new_x, new_y))
            visited.add((new_x, new_y))
if yes:
    print('YES')

else:
    print('NO')


