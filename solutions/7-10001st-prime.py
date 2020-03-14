from utils import prime_gen

if __name__ == '__main__':
    primes = prime_gen()
    for _ in range(10001):
        p = next(primes)

    print(p)
