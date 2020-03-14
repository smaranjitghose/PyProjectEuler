from collections import defaultdict
from math import factorial as fac

if __name__ == '__main__':
    # Dynamic programming method
    paths = defaultdict(dict)
    for i in range(21):
        paths[0][i] = 1
        paths[i][0] = 1
    for i in range(1, 21):
        for j in range(1, 21):
            paths[i][j] = paths[i-1][j] + paths[i][j-1]
    print(paths[20][20])

    # Pure math
    print(fac(40)//fac(20)//fac(20))
