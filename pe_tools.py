
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

def repeating_cf(cf):
    """
    takes a list of the form [a0, a1, a2, a3, ...]
    and interprets as a continued fraction of the form
    [a0; (a1, a2, a3, ...)] where (a1, a2, a3, ...) repeats
    and returns a generator which repeats that sequence
    indefinitely.
    """
    assert len(cf) > 1
    yield cf[0]
    cf = cf[1:]
    i = 0
    while True:
        yield cf[i]
        i = (i + 1) % len(cf)

def continued_fraction_sqrt(n):
    """
    returns a list [a0, a1, a2, a3,...]
    Which can be intepreted as a continued fraction of the form
    [a0; (a1, a2, a3, ...)]
    where (a1, a2, a3, ...) repeats indefinitely.
    Use repeating_cf to convert to an infinite generator
    of continued fraction terms.
    """
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
    
