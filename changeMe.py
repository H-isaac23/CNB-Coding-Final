def change_me(denomination, n):
    num_coins = 0
    for i in range(len(denomination)-1, -1, -1):
        while True:
            if n - denomination[i] == 0:
                num_coins += 1
                return f'{num_coins} coins'
            elif n - denomination[i] >= 0:
                num_coins += 1
                n -= denomination[i]
            else:
                break
    if n != 0:
        return None
    else:
        return f'{num_coins} coins'

print(change_me([1, 5, 10, 20], 39))
print(change_me([1, 5, 10, 20, 50], 213))
print(change_me([5, 10, 25], 69))
print(change_me([50], 50))
print(change_me([50, 100, 500, 1000], 362880))
