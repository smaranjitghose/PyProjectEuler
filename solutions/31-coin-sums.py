def coin_change(total, coins):
    if total == 0:
        return 1

    if total < 0:
        return 0

    if not coins and total > 0:
        return 0

    return coin_change(total-coins[0], coins) + coin_change(total, coins[1:])


if __name__ == '__main__':
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    total = 200
    ans = coin_change(total, coins)
