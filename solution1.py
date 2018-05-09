class Solution:
    def repeated(self, s):
        if len(set(list(s))) < len(s):
            return True
        return False
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        max_length = 0
        for i in range(length):
            for j in range(i + 1, length + 1):
                sub_string = s[i:j]
                if len(sub_string) > max_length and not self.repeated(sub_string):
                    max_length = len(sub_string)
        return max_length


s = Solution()
str = 'a'
print(s.lengthOfLongestSubstring(str))
