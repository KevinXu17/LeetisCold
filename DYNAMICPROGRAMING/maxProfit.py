# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
"""
    state + dp

"""

"""
    O(n) but with space O(n)
    can change to 4 pointers to only keep int then space O(1)
"""

class Solution:
    def maxProfit(self, prices) -> int:
        days = len(prices)
        # 4 states bug sell hold cooldown
        buys = [0] * days
        sells = [0] * days
        holds = [0] * days
        cooldowns = [0] * days
        buys[0] = -prices[0]
        holds[0] = -prices[0]
        for i in range(1, days):
            sells[i] = max(buys[i - 1], holds[i - 1]) + prices[i]

            cooldowns[i] = max(cooldowns[i - 1], sells[i - 1])

            holds[i] = max(holds[i - 1], buys[i - 1])

            buys[i] = cooldowns[i - 1] - prices[i]
        return max(sells[days - 1], cooldowns[days - 1])


    def maxProfit1(self, prices) -> int:
        days = len(prices)
        # 4 states bug sell hold cooldown
        sells = 0
        cooldowns = 0
        buys = -prices[0]
        holds = -prices[0]
        for i in range(1, days):
            buys_before, holds_before, cooldowns_before, sells_before = buys, holds, cooldowns, sells

            sells = max(buys_before, holds_before) + prices[i]

            cooldowns = max(cooldowns_before, sells_before)

            holds = max(holds_before, buys_before)

            buys = cooldowns_before - prices[i]
        return max(sells, cooldowns)


