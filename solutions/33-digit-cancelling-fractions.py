from fractions import Fraction
from functools import reduce
from operator import mul

def is_curious(num, den):
    if(num==den):
        return False
    num_s, den_s = str(num), str(den)
    if num_s[1] == den_s[1] == '0':
        return False
    try:
        if num_s[0] == den_s[0] and Fraction(num, den) ==Fraction(int(num_s[1]),int(den_s[1])):
            return True
        if num_s[1] == den_s[0] and Fraction(num, den) ==Fraction(int(num_s[0]),int(den_s[1])):
            return True
        if num_s[0] == den_s[1] and Fraction(num, den) ==Fraction(int(num_s[1]),int(den_s[0])):
            return True
        if num_s[1] == den_s[1] and Fraction(num, den) ==Fraction(int(num_s[0]),int(den_s[0])):
            return True
    except:
        pass
    return False

def find_curious():
    for num in range(11, 100):
        for den in range(num, 100):
            if is_curious(num, den):
                print(num, den)
                yield Fraction(num, den)


if __name__ == '__main__':
    g = find_curious()
    product = reduce(mul, g)
    print(product.denominator)
