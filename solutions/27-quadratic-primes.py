from utils import prime_gen
from utils import prime_factors

def number_of_consec_primes(a, b):
    n = 0
    while True:
        formula = n*n + a*n + b
        if sum(prime_factors(formula)) != formula:
            return n
        n += 1

if __name__ == '__main__':
    p = prime_gen()
    ps = []
    while True:
        prime = next(p)
        ps.append(prime)
        if prime > 1000:
            break
    results = [(a, b, number_of_consec_primes(a, b))
                for a in range(-1000, 1000)
                for b in ps]
    ans = max(results, key=lambda x: x[2])
    print(ans, ans[0]*ans[1])
