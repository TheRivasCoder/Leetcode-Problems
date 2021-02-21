t = "abba"


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic = {}
        longest = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                start = dic[s[i]] +1
                dic[s[i]] = i
            longest = max(longest, i-start+1)
        return longest

test = Solution()

print(test.lengthOfLongestSubstring(t))