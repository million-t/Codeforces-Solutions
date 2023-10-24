



t = int(input())
for _ in range(t):
    s = input()

    temp = ['']*100
    cur_ind = 50
    seen = set()
    no = False

    for char in s:
        if not temp[cur_ind]:
            temp[cur_ind] = char
        
        elif temp[cur_ind - 1] == char:
            cur_ind -= 1
        
        elif temp[cur_ind + 1] == char:
            cur_ind += 1
        
        elif not temp[cur_ind - 1] and char not in seen:
            temp[cur_ind - 1] = char
            cur_ind -= 1
        
        elif not temp[cur_ind + 1] and char not in seen:
            temp[cur_ind + 1] = char
            cur_ind += 1

        else:
            no = True
            break

        seen.add(char)

    if no:
        print('NO')
    
    else:
        print('YES')
        ans = []
        added = set()
        for char in temp:
            if char:
                added.add(char)
                ans.append(char)
        
        for _ord in range(ord('a'), ord('z') + 1):
            char = chr(_ord)
            if char not in added:
                ans.append(char)
        
        print("".join(ans))


