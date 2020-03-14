from utils import fibonacci_gen
import itertools
import timeit

def fib_gen(num=10000):
    n_minus_2 = 0
    n_minus_1 = 1
    for i in range(num):
        n = n_minus_2 + n_minus_1
        yield n
        n_minus_2 = n_minus_1
        n_minus_1 = n

def solve_1():
    fibs = fib_gen()
    even_fibs = (n for n in fibs if n % 2 == 0)
    small_even_fibs = filter(lambda x: x < 4000000, even_fibs)
    total = sum(small_even_fibs)
    return total

def solve_2():
    ans = sum(
            x for x in
            itertools.takewhile(
                lambda x: x < 4_000_000,
                fibonacci_gen()
                )
            if x % 2 == 0
            )
    return ans

if __name__ == '__main__':
    print(solve_1())
    print(solve_2())
