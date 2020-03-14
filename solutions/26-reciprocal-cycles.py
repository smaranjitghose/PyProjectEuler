"""Based on chillee's answer at Fri, 6 Jan 2017, 05:06:
There's so many convoluted substring solutions.

1/3 = 3/9 = 0.(3)
1/7 = 148257/999999 = 0.(148257)

Therefore, the length of the repeating portion is length of the numerator when
you set the denominator equal to some string of 9s.

There's one other thing to keep in mind, which is that 1/5 and 1/2 have
terminating decimals, as 5 and 2 are the only divisors of 10. So, for example,
1/6 = 1/3 * 1/2, and it's clear that the length of the repeating decimal is the
length of the repeating decimal of 1/3. And if the prime factors of the
denominator are only composed of 2's and 5's, the denominator is terminating.
"""


def cycle_length(x):
    while x % 2 == 0:
        x //= 2
    while x % 5 == 0:
        x //= 5
    if x == 1:
        return 0
    t = 9
    while True:
        if t % x == 0:
            return len(str(t))
        else:
            t = t * 10 + 9

if __name__ == '__main__':
    results = [(x, cycle_length(x)) for x in range(1, 1001)]
    print(max(results, key=lambda pair: pair[1]))
