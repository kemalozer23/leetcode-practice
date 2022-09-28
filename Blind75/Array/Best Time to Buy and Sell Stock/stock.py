class Solution:
    def maxProfit(self, prices):
        min_price_so_far, max_profit = max(prices), 0
        for price in prices:
            max_profit_se1l_today = price - min_price_so_far
            max_profit = max(max_profit, max_profit_se1l_today)
            min_price_so_far = min(min_price_so_far, price)
        return max_profit

    def maxProfit2(self, prices):
        res = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res


# Example 1:
prices1 = [7,1,5,3,6,4]
#---> Output 1: 5

# Example 2:
prices2 = [7,6,4,3,1]
#---> Output 2: 0

if __name__== "__main__":
    s = Solution()
    print("Output 1: ", s.maxProfit(prices1))
    print("Output 2: ", s.maxProfit(prices2))
    print("Output 1: ", s.maxProfit2(prices1))
    print("Output 2: ", s.maxProfit2(prices2))