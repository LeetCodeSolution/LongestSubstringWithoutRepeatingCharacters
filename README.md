# Longest Substring Without Repeating Characters

## 题目描述

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

## 解题思路

### 解法一

遍历所有的子序列，然后比较序列长度，找出最长的序列。

全部遍历的时间复杂度是O(n2)，所以比较耗时。

### 解法二

顺次遍历每个字符来构造新的子字符串，如果新的字符不存在于子字符串中，则将字符拼到子字符串后面。

如果存在，那么就先找到新的字符在子字符串的位置，然后将子字符串后面的一部分和新的字符拼合，形成新的子字符串。

```python
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
```
