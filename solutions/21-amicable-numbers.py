from utils import divisors

def amicable_pairs(stop=10000):
    d = {}
    for i in range(2, stop + 1):
        amicable_cand = sum(divisors(i))-i
        if i in d:
            if d[i] == amicable_cand:
                yield d[i], i
            else:
                d[amicable_cand] = i
        else:
            d[amicable_cand] = i


if __name__ == '__main__':
    ans = sum(sum(pair) for pair in amicable_pairs())
