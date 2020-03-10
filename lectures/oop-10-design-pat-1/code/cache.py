import time

class CachedRunner:
    def __init__(self, num_cached):
        self.num_cached = num_cached
        self.results = {}

    def __call__(self, f):
        self.f = f
        def wrapped_func(*args):
            args_tuple = tuple(args)
            if args_tuple not in self.results:
                self.results[args_tuple] = self.f(*args)
            return self.results[args_tuple]
        return wrapped_func

def timeit(f):
    def wrapped_func(*args):
        start_time = time.perf_counter()
        res = f(*args)
        print("Time taken {}".format(time.perf_counter() - start_time))
        return res
    return wrapped_func

@timeit
@CachedRunner(10)
def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return b

@timeit
@CachedRunner(10)
def fac(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

for i in range(100000, 100002):
    a = fib(i)
    b = fac(i)
    print("Processing for i = {} complete".format(i))
for i in range(100000, 100002):
    a = fib(i)
    b = fac(i)
    print("Second processing for i = {} complete".format(i))
