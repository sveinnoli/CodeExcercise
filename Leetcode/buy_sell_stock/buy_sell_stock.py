
class Solution:
    def maxProfit(self, prices):
        maxprofit=0
        lowest=prices[0]
        for i in range(1, len(prices)):
            if lowest > prices[i]:
                lowest = prices[i]
            else:
                currprofit = prices[i] - lowest
                if currprofit  > maxprofit:
                    maxprofit = currprofit
        return maxprofit



if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,11,1,2,4]))

       