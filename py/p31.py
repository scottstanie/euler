coins = [1, 2, 5, 10, 20, 50, 100, 200]


def count(coins, idx, n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif idx < 0 and n > 0:
        return 0
    else:
        return count(coins, idx - 1, n) + count(coins, idx, n - coins[idx])


if __name__ == '__main__':
    print count(coins, len(coins) - 1, 200)
