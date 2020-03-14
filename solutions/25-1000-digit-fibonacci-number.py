from utils import fibonacci_gen
import itertools

if __name__ == '__main__':
    for ind, fib in enumerate(fibonacci_gen(), 1):
        if len(str(fib)) == 1000:
            break
    print(ind, fib)
