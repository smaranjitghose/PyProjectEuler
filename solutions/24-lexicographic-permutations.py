import itertools

if __name__ == '__main__':
    perms = map(''.join, itertools.permutations('0123456789'))
    for i in range(1_000_000):
        ans = next(perms)
    print(ans)
