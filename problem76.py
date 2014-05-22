def good_decorator(d):
    def new_decorator(f):
        g = d(f)
        f.__name__ = f.__name__

@good_decorator
def memoized(f):

def find_summations(n):
    for i in range(1,n)[::-1]:

if __name__ == '__main__':
    
