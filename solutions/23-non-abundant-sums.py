from utils import sum_of_proper_divisors
import itertools

def is_abundant(num):
    return sum_of_proper_divisors(num) > num

def abundant_num_gen(start=12, stop=100000):
    for i in range(start, stop):
        if is_abundant(i):
            yield i

if __name__ == '__main__':
    abundants = abundant_num_gen(stop=28123)
    s = set(x + y for x, y in itertools.combinations_with_replacement(abundants, 2))
    ans = sum(num
              for num
              in range(1, 28124)
              if num not in s)
