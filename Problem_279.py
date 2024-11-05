class Solution:
    def numSquares(self, n: int) -> int:
        
        # create an array and store the numbers.
        # Like dp[4] = 1, dp[8] = 2, so on
        
        dp = [10001]*(n+1)
        
        dp[0] = 0
        
        i = 1
        while i <= n:
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], 1 + dp[i - j*j])
                j += 1
            i += 1
        
        #print(dp)
        
        return dp[n]
                
                
