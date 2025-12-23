"""
Module for calculating change using Greedy and Dynamic Programming algorithms.
"""
from collections import defaultdict
import timeit



def find_coins_greedy(amount: int, coins: list[int]) -> dict[int, int]:
    """
    Greedy algorithm to find the change for a given amount.
    Optimized to use division instead of repeated subtraction.
    """
    coins = sorted(coins, reverse=True)
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount %= coin
    return result


def find_min_coins(amount: int, coins: list[int]) -> dict[int, int]:
    """
    Dynamic programming algorithm to find the minimum number of coins for a given amount.
    Optimized: internal loop iterates through amounts for each coin.
    """
    # min_coins[i] stores the minimum number of coins needed for amount i
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    # coin_used[i] stores the last coin added to make amount i optimal
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    # If amount cannot be formed
    if min_coins[amount] == float('inf'):
        return {}

    # Reconstruct dictionary
    result = defaultdict(int)
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        result[coin] += 1
        current_amount -= coin

    return dict(sorted(result.items()))


def measure_time(func, amount, coins):
    """
    Measure the execution time of a function.
    """
    start_time = timeit.default_timer()
    func(amount, coins)
    return timeit.default_timer() - start_time


if __name__ == "__main__":
    coins_list = [50, 25, 10, 5, 2, 1]

    # Test cases to verify correctness
    TEST_AMOUNT = 113
    print("-" * 20)
    print(f"Testing amount {TEST_AMOUNT}:")
    print(f"Greedy: {find_coins_greedy(TEST_AMOUNT, coins_list)}")
    print(f"DP:     {find_min_coins(TEST_AMOUNT, coins_list)}")
    print("-" * 20)

    # Performance comparison
    amounts_list = [113, 1000, 2000, 5000]

    print(f"{'Amount':<10} | {'Greedy Time (s)':<20} | {'DP Time (s)':<20}")
    print("-" * 55)

    for amount_item in amounts_list:
        # For very large amounts, DP can be slow due to memory/time, so be careful raising too high
        greedy_time = measure_time(find_coins_greedy, amount_item, coins_list)
        dp_time = measure_time(find_min_coins, amount_item, coins_list)

        print(f"{amount_item:<10} | {greedy_time:<20.6f} | {dp_time:<20.6f}")

    coins_list = [9, 6, 1]
    TEST_AMOUNT = 12
    print()
    print("-" * 20)
    print(f"Testing coins {coins_list}")
    print(f"Testing amount {TEST_AMOUNT}:")
    print(f"Greedy: {find_coins_greedy(TEST_AMOUNT, coins_list)}")
    print(f"DP:     {find_min_coins(TEST_AMOUNT, coins_list)}")
    print("-" * 20)
