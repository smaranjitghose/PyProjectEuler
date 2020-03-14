from functools import lru_cache

def sequence(n):
    'bad idea'
    while n is not 1:
        yield n
        n = 3*n+1 if n%2 else n/2
    yield n

def next_num(n):
    if n % 2:
        return 3 * n + 1
    else:
        return n / 2

@lru_cache(None)
def collatz_length(n):
    if n == 1:
        return 1
    else:
        return 1 + collatz_length(next_num(n))

if __name__ == '__main__':
    i = 0
    largest = 0
    for n in range(1, 1_000_001):
        length = collatz_length(n)
        if length > largest:
            largest = length
            i = n
    print(i, largest)
