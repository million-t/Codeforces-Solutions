tests = int(input())

for _ in range(tests):
    input()

    num_cells, k = map(int, input().split())

    positions = list(map(int, input().split()))
    temps = list(map(int, input().split()))


    res = [float('inf')]*(num_cells)

    for p, t in zip(positions, temps):
        res[p - 1] = t
    
    for ind in range(1, num_cells):
        res[ind] = min(res[ind- 1] + 1, res[ind])
        res[~ind] = min(res[~(ind- 1)] + 1, res[~ind])


    print(*res)