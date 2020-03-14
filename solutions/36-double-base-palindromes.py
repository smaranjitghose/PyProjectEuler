from utils import palindrom

def double_base_palindromes(cap=1000):
    for n in range(cap):
        if palindrom(str(n)) and palindrom('{0:b}'.format(n)):
            yield n

if __name__ == '__main__':
    ans = sum(double_base_palindromes(1000000))
