# Neetcode.io solution

# Time complexity: O(n) - iterates once over the prices
# Space complexity: O(1) - no extra space is required

def maxProfit(prices):
    # Stores the max diff between buy and sell
    profit = 0
    # Starts with the first value in the array
    lowest = prices[0]

    # For each price in the array, if it is lower than
    # the previous lowest value, you update the variable.
    # If it's not lower, it means that the current price
    # will produce a profit as it is bigger than the
    # the price at which it was bought (lowest). However,
    # if it is lower, it means that we can start checking
    # if with the following numbers we can get more profit.
    # It's important to keep in mind that each time we
    # calculate the max from the previous profit and the new
    # one, so even if no bigger profit is found after
    # updating the new lowest, we still save the previous
    # biggest profit
    for price in prices:
        # If the current prices is lower than the previous
        # lowest, we update it
        if price < lowest:
            lowest = price
        # Always calculate the profit and get the max from
        # the previous profit and the new one
        profit = max(profit, price - lowest)
    return profit

print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1])) # 0