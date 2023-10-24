from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    lens_map = defaultdict(list)
    strings = []
    for _ in range(n):
        string = input()
        strings.append(string)
        lens_map[len(string)].append(string)
    
    for st in strings
