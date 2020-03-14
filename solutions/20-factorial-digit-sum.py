from math import factorial


if __name__ == '__main__':
    ans = sum(map(int, str(factorial(100))))
    print(ans)
