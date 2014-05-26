
def approx_int_sqrt(n):
    import math
    return int(math.sqrt(n))

def cf_to_rational(cf):
    from fractions import Fraction
    cf = cf[::-1]
    c = Fraction(cf[0], 1)
    for a in cf[1:]:
        c = Fraction(a) + Fraction(c.denominator, c.numerator)
    return c

def continued_fraction_sqrt(n):
    a = a0 = approx_int_sqrt(n)
    m = 0
    d = 1
    sequence = []
    while True:
        m = d*a - m
        d = (n - m*m) / d
        a = (a0 + m) / d
        next_triple = (a, d, m)
        if next_triple in sequence:
            return [a0] + [x[0] for x in sequence]
        sequence.append(next_triple)

def is_square(n):
    h = n & 0xF
    if h in [0,1,4,9]:
        from math import sqrt
        s = int(sqrt(n))
        return n == s*s
    return False
    
