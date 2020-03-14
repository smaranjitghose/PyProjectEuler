if __name__ == '__main__':
    ans = len(set(a**b
                  for a in range(2, 101)
                  for b in range(2, 101)))
