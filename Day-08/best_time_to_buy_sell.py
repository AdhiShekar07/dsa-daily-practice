"""
Problem: Best Time to Buy and Sell Stock
Platform: LeetCode
Difficulty: Easy
Approach: Greedy
Time Complexity: O(n)
Space Complexity: O(1)
"""

prices = list(map(int, input("Enter prices: ").split()))

min_price = prices[0]
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

print("Maximum Profit:", max_profit)
