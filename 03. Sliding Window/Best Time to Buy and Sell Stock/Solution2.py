# Time complexity: O(n) - iterates once over the prices
# Space complexity: O(1) - no extra space is required

# Two pointer solution

def maxProfit(prices):
    profit, buyIndex, sellIndex = 0, 0, 0

    for i in range(len(prices)):
        if i > 0:
            # Move buy if current number is less than
            # previous buy value. When moving buy,
            # move to the same position sell
            if prices[i] < prices[buyIndex]:
                buyIndex = i
                sellIndex = i
            # Move sell if the current number is
            # greater than the previous sell
            elif prices[i] > prices[sellIndex]:
                sellIndex = i
            # Each time calculate sell-buy and get the
            # max from the previous profit and the new
            profit = max(profit, prices[sellIndex] - prices[buyIndex])
    return profit

print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1])) # 0