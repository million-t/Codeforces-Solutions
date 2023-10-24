l, r = map(int, input().split())


if l == r:

    print(0)


else:

    xor = r^l

    b = 1 << xor.bit_length() - 1


    a = 0

    for i in range(xor.bit_length() - 1):
        a <<= 1
        a ^= 1


    print(b^a)

