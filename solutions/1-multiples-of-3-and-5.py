from itertools import chain

def threes_and_fives_gen(num=1000):
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            yield i

def threes_and_fives_fun(n):
    return set(chain(range(3, n+1, 3), range(5, n+1, 5)))

def solve(n):
    return sum(
        filter(lambda x: x%3==0 or x%5==0,
               range(1, n)
        )
    )

def solve_2(n):
    return sum(
            x
            for x in range(1, n)
            if x%3==0 or x%5==0
    )

if __name__ == '__main__':
    print(solve_2(1000000))
