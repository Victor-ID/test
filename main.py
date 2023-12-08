def extended_euclidian(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_euclidian( b % a, a)

    x = y1 - (b/a) * x1 # we use integer division here
    y = x1

    return gcd, x, y
