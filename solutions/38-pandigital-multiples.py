def pandigital_multiples():
    for n in range(1, 10000):
        s = set('123456789')
        mul = 1
        while s:
            try:
                for digit in str(n*mul):
                    s.remove(digit)
            except KeyError:
                break
            mul += 1
        if len(s)==0 and mul > 1:
            yield n, mul-1

if __name__ == '__main__':
    g = pandigital_multiples()
    for n in g:
        print(n)

