def rearrange(chorus):
    output = ['']*len(chorus)
    for word in chorus:
        temp = ''
        ind = 0
        for charac in word:
            if charac.isnumeric():
                ind = int(charac) - 1
            else:
                temp += charac
        output [ind] = temp
    return output



test_cases = int(input())

for _ in range(test_cases):
    chor = input().split(' ')
    print(' '.join(rearrange(chor)))


