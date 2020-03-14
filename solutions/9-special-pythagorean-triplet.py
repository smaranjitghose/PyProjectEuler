if __name__ == '__main__':
    triplets = ((a, b, c)
                for c in range(500, 1, -1)
                for b in range(c, 1, -1)
                for a in range(b, 1, -1))
    for a, b, c in triplets:
        if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
            print(a, b, c, a*b*c)
            break
