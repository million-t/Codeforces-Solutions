def build_suffix_array(s):
    n = len(s)
    suffixes = []
    for ind in range(n):
        suffixes.append((s[ind:], ind))

    suffixes.sort()
    suffix_array = []
    for suffix, start in suffixes:
        suffix_array.append(start)
    
    return suffix_array


s = input() + '#'
print(*build_suffix_array(s))