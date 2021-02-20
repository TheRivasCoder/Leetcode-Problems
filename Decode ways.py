number = '13242234109'

class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        variations = [0]*(len(s)+1)
        variations[0] = 1
        for i in range(len(s)+1):
            if s[i-1] != '0':
                variations[i] += variations[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                variations[i] += variations[i-2]
        return variations[-1]

test = Solution()

print(test.numDecodings(number))
        