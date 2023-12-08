def extended-euclidian(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended-euclidian( b mod a, a)

    x = y1 - (b/a) * x1 # we use integer division here
    y = x1

    return gcd, x, y
