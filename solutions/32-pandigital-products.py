from itertools import permutations

def pandigital_products_fun():
    for p in permutations('123456789*='):
        equation = ''.join(p).replace('=','==')
        if equation.index('*') > equation.index('=='):
            continue
        try:
            ans = eval(equation)
            if ans:
                print(equation)
                number = int(equation.split('==')[-1])
                yield number
        except:
            continue

def is_pandigital(n):
    if len(n) == 9:
        if '1' in n and '2' in n and '3' in n and '4' in n and '5' in n and\
           '6' in n and '7' in n and '8' in n and '9' in n:
               return True
    return False

def pandigital_products_numerical():
    for x in range(1, 100):
        for y in range(1, 10000):
            product = x * y
            if is_pandigital(str(x) + str(y) + str(product)):
                yield product

if __name__ == '__main__':
    g = pandigital_products_numerical()
    print(sum(set(g)))
