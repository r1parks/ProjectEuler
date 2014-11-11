#!/usr/bin/env python

import time

divisors_list = [0]

#max_list = []

def d(n):
    import primes
    if n <= 1:
        return 0
    factors = primes.smallFactorGen(n)
    ans = 1
    for _,x in factors:
        ans *= x+1
    return ans

def print_info(max_list):
    import primes
    s = set(max_list)
    print s
    if all(map(lambda n: n %2 == 0, s)):
        print "all divisible by 2"
    lrg_factors = []
    for n in s:
        lrg_factors.append(max(list(primes.factorGen(n)), key=lambda x: x[0])[0])
    print "largest factors: {}".format(sorted(lrg_factors))

def gen_max_list(u, k):
    print "making max list!"
    start = time.clock()
    #global max_list
    current_max = 0
    current_max_index = -1
    n = 0
    while n + k <= u: 
        if n > current_max_index:
            #max_list.append(max(divisors_list))
            current_max = max(divisors_list)
            yield(current_max)
            #current_max_index = divisors_list.index(max_list[-1])+n
            current_max_index = divisors_list.index(current_max)+n
        else:
            next_div = divisors_list[-1]
            #if next_div > max_list[-1]:
            if next_div > current_max:
                current_max_index = n+k-1
                #max_list.append(next_div)
                current_max = next_div
                yield current_max
            else:
                #max_list.append(max_list[-1])
                yield current_max
        n+=1
        if n % 100000 == 0:
            new_time = time.clock()
            print "{}: {}sec".format(n, new_time - start)
            start = new_time
        divisors_list.append(d(n+k))
        divisors_list.pop(0)
    #print_info(max_list)
    print "max list took {} sec".format(time.clock() - start)

def init_div_list(limit):
    print "making divisors list!"
    start = time.clock()
    global divisors_list
    while(len(divisors_list) < limit):
        n = len(divisors_list)
        if n % 2 != 0 and n % 3 != 0:
            divisors_list.append(1)
        else:
            divisors_list.append(d(n))
    print "divisors list took {} sec".format(time.clock() - start)

def M(n, k):
    global divisors_list
    return max(divisors_list[n:n+k])

def S(u, k):
    global divisors_list
    init_div_list(k)
    #gen_max_list(u, k-1)
    #return sum(max_list[1:])
    g = gen_max_list(u, k-1)
    g.next()
    return sum(g)

if __name__ == '__main__':
    print S(100000000, 100000)
    #print  S(100000, 1000)
