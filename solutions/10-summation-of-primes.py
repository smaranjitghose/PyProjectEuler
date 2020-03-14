"Prime number generator"

def gen(cap=2000000):
    all_primes = []
    def is_prime(i):
        for p in all_primes:
            if p > i ** 0.5:
                return True
            if i % p == 0:
                return False
        return True
    for i in range(2, cap):
        if is_prime(i):
            all_primes.append(i)
            yield i

if __name__ == '__main__':
    print(sum(gen()))
