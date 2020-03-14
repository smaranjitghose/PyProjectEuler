print(
    max(
        ( i * j
        for i in range(999, 100, -1)
        for j in range(i, 100, -1)
        if str(i*j) == str(i*j)[::-1])))
