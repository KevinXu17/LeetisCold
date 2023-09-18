

def maxProfit(prices):
    min_pivot = 0
    diff = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[min_pivot]:
            min_pivot = i
        else:
            diff = max(diff, prices[i] - prices[min_pivot])
    return diff




print(maxProfit([7,1,5,3,6,4]))
