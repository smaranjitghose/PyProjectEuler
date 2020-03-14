from utils import prime_gen

prime_set = set()
prime_set.add('')


def is_trunc(number: str):
    for i in range(len(number)):
        if number[i:] not in prime_set:
            return False
    for i in range(len(number)):
        if number[:-i] not in prime_set:
            return False
    return True


def two_sided_trunc_primes():
    primes = prime_gen()
    while True:
        p = str(next(primes))
        prime_set.add(p)
        if is_trunc(p):
            yield int(p)


if __name__ == '__main__':
    g = two_sided_trunc_primes()
