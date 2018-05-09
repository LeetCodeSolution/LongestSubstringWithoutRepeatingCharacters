class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        str = ''
        for i in range(len(s)):
            if not s[i] in str:
                str += s[i]
            else:
                str = str[str.index(s[i]) + 1:i] + s[i]
            if len(str) > max_length:
                max_length = len(str)
        return max_length


s = Solution()
str = 'pwwkew'
print(s.lengthOfLongestSubstring(str))
