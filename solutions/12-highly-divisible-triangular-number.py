from utils import prime_factors
from utils import triangular_gen
from itertools import count
from collections import Counter
from functools import reduce
from operator import mul
from collections import defaultdict

if __name__ == '__main__':
    g = triangular_gen()
    next(g)
    for tri in g:
        c = Counter(prime_factors(tri))
        factors = reduce(mul, map(lambda x: x+1, c.values()))
        if factors >= 500:
            print(tri)
            break
