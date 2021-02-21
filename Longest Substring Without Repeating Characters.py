test = "abba"

def lengthOfLongestSubstring(s: str) -> int:
    dic = {} #Dictionary to check if we have encountered same letter before
    longest = 0
    start = 0
    for index in range(len(s)):
        if s[index] not in dic: #Check if current letter is NOT in dictionary
            dic[s[index]] = index #Add letter and it's index to dictionary
        else:
            start = max(start, dic[s[index]] +1) #If letter in dictionary, move start to index after repeated letter
            dic[s[index]] = index #Update index of repeated letter
        longest = max(longest, index-start+1) #Longest string is equal to the largest between previous longest string or current string length
    return longest


print(lengthOfLongestSubstring(test))