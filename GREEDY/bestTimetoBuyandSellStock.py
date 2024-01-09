# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

'''
    greedy => min_price before current price
'''
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

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# easy one: greedy => sell if it has profit
# class Solution {
# public:
#     int maxProfit(vector<int>& prices) {
#         int profit = 0;
#         for (size_t i = 1; i < prices.size(); i ++) {
#             if (prices[i] - prices[i-1] > 0) {
#                 profit = profit + prices[i] - prices[i-1];
#             }
#         }
#         return profit;
#     }
# };