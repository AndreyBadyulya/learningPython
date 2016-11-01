import time

def timer(f):
    def tmp(*args):
        start_f = time.time()
        result = f(*args)
        end_f = time.time()
        print 'Execution time was: %f' %(end_f - start_f)
        return result
    return tmp

@timer
def reduce_factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))

@timer
def recurs_factorial(n):
    def recursia(n):
        return 1 if n == 0 else  n * recurs_factorial(n - 1)
    return recursia

@timer
def my_factorial(n):
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

print reduce_factorial(100)
print recurs_factorial(100)
print my_factorial(100)