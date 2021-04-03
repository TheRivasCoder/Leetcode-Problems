


class Solution:
    def numDecodings(self, s: str) -> int:
        return self.helper(0, s)

    def helper(self, index, s):
        
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1
        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0
        if index == len(s)-1:
            return 1
        
        answer = self.helper(index + 1, s)
        if int(s[index : index + 2]) <= 26:
            answer += self.helper(index + 2, s)
        return answer
        