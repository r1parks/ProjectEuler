#!/usr/bin/env python

import math
import pe_tools
from pe_tools import continued_fraction_sqrt

if __name__ == '__main__':
    total = 0
    for i in range(1, 10000):
        if not pe_tools.is_square(i):
            l = len(continued_fraction_sqrt(i)) - 1
            if l % 2 == 1:
                total+=1
    print str(total)
