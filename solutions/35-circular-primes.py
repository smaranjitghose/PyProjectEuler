from utils import prime_gen

def rotate(l):
    for x in range(len(l)):
        yield l[-x:] + l[:-x]

def circular_primes():
    p = prime_gen()
    while True:
        prime = next(p)
        if prime > 1_000_000:
            break
        else:
            s.add(str(prime))
    for prime in s:
        if all((''.join(p) in s)
                for p in rotate(prime)):
            yield int(prime)


if __name__ == '__main__':
    s = set()
    ans = len(list(circular_primes()))

