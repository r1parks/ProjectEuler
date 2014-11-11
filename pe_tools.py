
def normal_vector(p1, p2):
    """
    returns the vector p1->p2 in normalized form: 
    a*i + b*j + c*k = (a, b, c)
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x2-x1, y2-y1, z2-z1)

def cross_product(u, v):
    """
    vectors of the form (u1, u2, u3), (v1, v2, v3)
    """
    u1, u2, u3 = u
    v1, v2, v3 = v
    return ((u2*v3 - u3*v2), (u3*v1 - u1*v3), (u1*v2 - u2*v1))

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
    
def decorator_function(d):
    def new_decorator(f):
        g = decorator(f)
        g.__name__ = f.__name__
        g.__doc__ == f.__doc__
        g.__dict__.update(f.__dict__)
        return g
    new_decorator.__name__ = d.__name__
    new_decorator.__doc__ = d.__doc__
    new_decorator.__dict__.update(d.__dict__)
    return new_decorator

class decorator_class(object):
    def __init__(self, f):
        self.__name__ = f.__name__
        self.__doc__ == f.__doc__
        self.__dict__.update(f.__dict__)
        

class memoized(decorator_class):
    def __init__(self, f):
        super(memoized, self).__init__(f)
        self.func = f
        self.cache = {}

    def __call__(self, *args):
        key = str(args)
        if key not in self.cache:
            self.cache[key] = self.func(*args)
        return self.cache[key]

def nCr(n, r):
    assert(r <= n)
    if n > 100:
        return nCr_big(n, r)
    else:
        return nCr_mem(n, r)

@memoized
def nCr_mem(n, r):
    if r == 0 or n == r:
        return 1
    return nCr_mem(n-1, r-1) + nCr_mem(n-1, r)

def nCr_big(n, r):
    if r > n/2:
        r = n - r
    ans = 1
    for i in range(1,r+1):
        ans *= n - r + i
        ans /= i
    return ans

def numDivisors(n):
    import primes
    if n <= 1:
        return 0
    factors = primes.factorGen(n)
    ans = 1
    for _,x in factors:
        ans *= x+1
    return ans

def divisorGen(n):
    import primes
    factors = list(primes.factorGen(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return
