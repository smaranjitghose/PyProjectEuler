from itertools import count
from math import factorial
from functools import reduce

def curious():
    for i in count():
        if sum(map(lambda x: factorial(int(x)), str(i))) == i:
            yield i
