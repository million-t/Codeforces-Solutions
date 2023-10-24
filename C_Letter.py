letter = input()



pref = []

lower = 0

for let in letter:
    pref.append(lower)
    if let.islower():
        lower += 1

suf = [0]*len(letter)
upper = 0

length = len(letter)
for ind, let in enumerate(letter[::-1]):
    suf[length - ind - 1] = upper
    if let.isupper():
        upper += 1


_min = float('inf')
for a, b in zip(pref, suf):
    _min = min(_min, a + b)

print(_min)
