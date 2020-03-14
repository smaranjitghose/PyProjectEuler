def spiral_diag_numbers(n):
    yield 1
    lvl = 1
    while True:
        width = lvl * 2 + 1
        last = width ** 2
        step = 2*lvl
        if width > n:
            break
        yield from range(last, last-3*step-1, -step)
        lvl += 1

if __name__ == '__main__':
    # first attempt
    # ans = sum(spiral_diag_numbers(5))

    # second attemp
    # for layer k, the side length is: n = 2*k + 1
    # corners of each layer
    # top right: n**2
    # top left: n**2 - n + 1
    # bottom left: n**2 - 2n + 2
    # bottom right: n**2 - 3n + 3
    # sum of four corners: 4*n**2 - 6n + 6
    ans = 1 + sum(4 * n ** 2 - 6 * n + 6
                  for n
                  in range(3, 1003, 2))
