number = '13242234109'

class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and "09"< s[i-2:i] < "27" : 
                # print(s[i-2:i])
                dp[i] += dp[i-2]
        print(dp)
        return dp[-1]

test = Solution()

print(test.numDecodings(number))
        