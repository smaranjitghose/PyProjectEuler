from collections import Counter, defaultdict
from functools import reduce
from operator import mul
from utils import prime_factors


if __name__ == '__main__':
    d = defaultdict(int)
    counters = (Counter(prime_factors(i)) for i in range(1, 21))
    for c in counters:
        d.update({k: max(v, d[k]) for k, v in c.items()})
    ans = reduce(mul, (k**v for k,v in d.items()))
    print(ans)
