# easy
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        h = len(haystack)
        n = len(needle)
        if n>h:
            return -1
        for i in range(h-n+1):
            if needle[0] == haystack[i]:
                j = 1
                while j < n and haystack[i+j] == needle[j]:
                     j = j + 1
                if j == n:
                    return i
        return -1
