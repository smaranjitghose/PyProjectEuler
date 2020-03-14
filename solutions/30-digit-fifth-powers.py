if __name__ == '__main__':
    ans = []
    for i in range(2, 6*9**5):
        digits = map(int, str(i))
        if i == sum(map(lambda x: x**5, digits)):
            print(i)
            ans.append(i)
    print(sum(ans))
