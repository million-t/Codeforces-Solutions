t = int(input())
for _ in range(t):
    n = int(input())
    word = input()

    replaced = {}

    yes = True
    for i, char in enumerate(word):
        if char in replaced:
            if replaced[char] != i%2:
                yes = False
                break

        else:
            replaced[char] = i%2

    if yes:
        print('YES')

    else:
        print('NO')  