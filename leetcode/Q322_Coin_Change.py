from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp = [ -1 for i in range(amount+1)]
        m_c= min(coins)
        if amount>0 and m_c<=amount:
            for coin in coins:
                if coin<=amount:
                    dp[coin] = 1
            for i in range(min(coins)+1,amount+1):
                min_coin = dp[i] if dp[i]!=-1 else float('inf')

                for j in range(len(coins)):
                    coin = coins[j]
                    if i-coin>=0:
                        if dp[i-coin]>0:
                            min_coin = min(dp[i-coin]+1,min_coin)
                if min_coin== float("inf"):
                    dp[i]=-1
                else:
                    dp[i] = min_coin

            return dp[-1]
        else:
            return -1

s= Solution()
coins = [1,2]
amount = 2
print(s.coinChange(coins,amount))